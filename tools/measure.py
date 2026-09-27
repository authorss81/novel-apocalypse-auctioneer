#!/usr/bin/env python3
"""Counting-motif detector + audits for The Apocalypse Auctioneer.

Calibrated against the closed Volume 05 block before it is used on Volume 06.
Run:  python3 tools/measure.py calib    # Chapters 241-250 (known block)
      python3 tools/measure.py block    # Chapters 251-260 (this block)
"""
import re
import sys
import os
import json
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CANON_PHRASES = [
    "counted it and got",
    "was counted and got",
    "counted what he said and got",
    "counted what she said and got",
    "the count came to",
    "it came to",
    "came to",
]

UNITS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
    "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
    "hundred": 100, "thousand": 1000,
}
MULT = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
        "seventy": 70, "eighty": 80, "ninety": 90}

WORDNUM = re.compile(r"^[a-z-]+$")


def words_to_num(tok):
    """'two hundred and eleven' -> 211 ; 'forty-eight' -> 48 ; 'forty' -> 40."""
    parts = [p for p in re.split(r"[\s-]+", tok.strip().lower()) if p]
    if not parts:
        return None
    if not all(WORDNUM.match(p) for p in parts):
        return None
    if any(p not in UNITS for p in parts):
        return None
    total = 0
    current = 0
    seen = False
    for p in parts:
        if p == "and":
            continue
        v = UNITS[p]
        if v >= 100:
            if current == 0:
                current = 1
            total += current * v
            current = 0
        elif v >= 20:
            current += v
        else:
            current += v
        seen = True
    if not seen:
        return None
    return total + current


def speech_paragraphs(lines):
    """A printed speech: a non-header, non-rule, non-document line whose whole
    content is a quoted bold run, e.g.  "**Four generations of ...**"  """
    out = []
    for i, ln in enumerate(lines):
        s = ln.strip()
        if not s or s.startswith("#") or s == "---" or s.startswith(">"):
            continue
        s = s.strip('"').strip()
        if s and s == s.upper() and re.search(r"[A-Z]", s):
            continue  # all-caps restatement at the foot of the chapter
        if s.startswith("**") and s.endswith("**") and len(s) > 4:
            out.append((i, s[2:-2]))
    return out


def count_sentence_words(body):
    """Words separated by spaces, hyphenated numeral is one word, trailing
    full stop not counted."""
    b = body.strip()
    b = b.rstrip(".")
    toks = b.split()
    return len(toks)


def find_claims(lines):
    """Yield (claim_number, phrase, line_index) for every class-one claim.

    Longest phrase first, and each match region is consumed so that
    'the count came to X' is not also reported as 'came to X'."""
    claims = []
    ordered = sorted(CANON_PHRASES, key=len, reverse=True)
    for i, ln in enumerate(lines):
        low = ln.lower()
        taken = [False] * len(low)
        hits = []
        for ph in ordered:
            start = 0
            while True:
                j = low.find(ph, start)
                if j < 0:
                    break
                start = j + 1
                if any(taken[j:j + len(ph)]):
                    continue
                n = parse_number_after(low, j + len(ph))
                if n is None:
                    continue
                for k in range(j, j + len(ph)):
                    taken[k] = True
                hits.append((j, n, ph))
        hits.sort()
        for _, n, ph in hits:
            claims.append((n, ph, i))
    return claims


def parse_number_after(low, pos):
    mm = re.match(r"\s+([a-z][a-z-]*(?:[\s-]+(?:and[\s-]+)?[a-z-]+)*)", low[pos:])
    if not mm:
        return None
    toks = [t for t in mm.group(1).split() if t != "and"]
    if not toks:
        return None
    if toks[0] == "a":
        toks = toks[1:]
    keep = []
    for t in toks:
        if words_to_num(t) is None:
            break
        keep.append(t)
    if not keep:
        return None
    return words_to_num(" ".join(keep))


def class_two(lines):
    """Claims of the form 'in N words'."""
    out = []
    for i, ln in enumerate(lines):
        for m in re.finditer(r"\bin ([a-z-]+(?:[\s-]+and[\s-]+[a-z-]+)*) words\b",
                             ln.lower()):
            n = words_to_num(m.group(1))
            if n is not None:
                out.append((i, n, ln.strip()[:90]))
    return out


def load(vol, nums):
    files = []
    for n in nums:
        p = os.path.join(ROOT, "chapters", vol, "chapter-%04d.md" % n)
        files.append((n, open(p, encoding="utf-8").read().split("\n")))
    return files


def resolve(files):
    """Resolve each claim forward to the next speech paragraph."""
    per_ch = {}
    mismatches = []
    detail = []
    for num, lines in files:
        sp = speech_paragraphs(lines)
        cl = find_claims(lines)
        sp_i = 0
        rows = []
        for n, ph, li in cl:
            # forward: first speech paragraph at index > li
            tgt = None
            for k in range(sp_i, len(sp)):
                if sp[k][0] > li:
                    tgt = sp[k]
                    sp_i = k + 1
                    break
            if tgt is None:
                mismatches.append((num, n, "no speech forward"))
                rows.append((n, "NO-TARGET", 0))
                continue
            got = count_sentence_words(tgt[1])
            rows.append((n, got, tgt[0] + 1))
            if got != n:
                mismatches.append((num, n, "paragraph=%d" % got))
        per_ch[num] = rows
        detail.append((num, rows))
    return per_ch, mismatches, detail


def denom(files):
    toks = []
    for num, lines in files:
        for ln in lines:
            if ln.startswith("#"):
                continue
            if ln.strip() == "---":
                continue
            s = ln
            s = s.replace("**", "")
            s = re.sub(r"^>\s?", " ", s)
            toks.extend(s.split())
    return sum(1 for t in toks if re.search(r"[A-Za-z0-9]", t))


def twelve_word_runs(files):
    seen = defaultdict(set)
    for num, lines in files:
        for ln in lines:
            s = ln.strip()
            if not s or s.startswith("#") or s == "---":
                continue
            s = s.replace("**", "")
            s = re.sub(r"^>\s?", " ", s)
            s = s.lower()
            s = re.sub(r"[^a-z0-9']+", " ", s)
            w = s.split()
            for i in range(len(w) - 11):
                seen[num].add(" ".join(w[i:i + 12]))
    counts = Counter()
    for num, s in seen.items():
        for run in s:
            counts[run] += 1
    shared = [r for r, c in counts.items() if c > 1]
    return len(shared)


def identical_paragraphs(files, minwords=12):
    paras = defaultdict(list)
    for num, lines in files:
        for ln in lines:
            s = ln.strip()
            if not s or s.startswith("#") or s == "---":
                continue
            s = s.replace("**", "")
            s = re.sub(r"[^a-z0-9 ]+", " ", s.lower())
            w = s.split()
            if len(w) >= minwords:
                paras[" ".join(w)].append((num, lines.index(ln) + 1))
    return {k: v for k, v in paras.items() if len(v) > 1}


def bold_clauses(files):
    out = {}
    for num, lines in files:
        n = sum(len(re.findall(r"\*\*", ln)) // 2 for ln in lines)
        out[num] = n
    return out


def footer_support(files):
    bad = []
    for num, lines in files:
        foot = None
        for i, ln in enumerate(lines):
            s = ln.strip()
            if s and s == s.upper() and re.search(r"[A-Z]", s) and not s.startswith("#"):
                foot = (i, s)
        if not foot:
            continue
        fi, ftxt = foot
        body = " ".join(lines[:fi]).lower()
        for phrase in re.findall(
                r"\b(?:twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|"
                r"one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
                r"thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|"
                r"hundred|thousand|first|second|third|fourth|fifth|sixth|seventh|"
                r"eighth|ninth|tenth)[a-z-]*", ftxt.lower()):
            if phrase not in body:
                bad.append((num, fi + 1, phrase))
    return bad


RESERVED = ["Iven", "Tallow", "First House", "Common Measure", "Custodian",
            "Morrow", "Verdict", "Orchard", "Selik", "Marne", "Cael", "Orin",
            "Crownless", "Uplands", "Upland", "Halloway", "Orrin", "Vale",
            "Quill", "Kest", "Lina", "Alder Reach", "Adrian", "Mara",
            "Brass", "Midnight", "Noon", "midnight", "noon", "overnight",
            "kilomet", "metric", "guarantor", "Uplands"]
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
            "Sunday", "monday", "tuesday", "wednesday", "thursday", "friday",
            "saturday", "sunday"]


def reserved_scan(files):
    hits = {}
    blob = []
    for num, lines in files:
        blob.append((num, " ".join(lines).lower()))
    for t in RESERVED:
        found = []
        for num, txt in blob:
            c = len(re.findall(r"\b" + re.escape(t.lower()) + r"\b", txt))
            if c:
                found.append((num, c))
        if found:
            hits[t] = found
    return hits


def integrity(files):
    out = []
    for num, lines in files:
        txt = "\n".join(lines)
        checks = {
            "doubled full stop": len(re.findall(r"\.\.", txt)),
            "doubled space": len(re.findall(r"[^\n] {2}", txt)),
            "trailing whitespace": len(re.findall(r"[ \t]+\n", txt)),
            "comma without space": len(re.findall(r",[A-Za-z]", txt)),
            "period without space": len(re.findall(r"\.[A-Za-z]", txt)),
            "tab": txt.count("\t"),
            "three dot": len(re.findall(r"\.\.\.", txt)),
            "colon time": len(re.findall(r"\d:\d\d", txt)),
            "twenty four hour": len(re.findall(r"\b(?:[01]\d|2[0-3]):[0-5]\d\b", txt)),
        }
        for k, v in checks.items():
            if v:
                out.append((num, k, v))
        for w in WEEKDAYS:
            if re.search(r"\b" + w + r"\b", txt):
                out.append((num, "weekday " + w, 1))
    return out


def wc(files):
    out = {}
    total = 0
    for num, lines in files:
        p = os.path.join(ROOT, "chapters", files_v(files, num), "chapter-%04d.md" % num)
        n = len(open(p, encoding="utf-8").read().split())
        out[num] = n
        total += n
    return out, total


def files_v(files, num):
    for vol, nums in files:
        pass
    return VOLMAP[num]


VOLMAP = {}


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "block"
    if mode == "calib":
        vol, nums = "volume-05", list(range(241, 251))
    elif mode == "pending":
        vol, nums = "volume-06", list(range(251, 261))
    else:
        vol, nums = "volume-06", list(range(251, 261))
    for n in nums:
        VOLMAP[n] = vol
    files = load(vol, nums)
    if mode == "pending":
        for num, lines in files:
            slots = re.findall(r"\[\[C\d+\]\]", "\n".join(lines))
            print("--- chapter", num, "slots:", len(slots))
            for i, body in speech_paragraphs(lines):
                print("   line %4d  words=%3d  %s" % (
                    i + 1, count_sentence_words(body), body[:60]))
        return
    per_ch, mism, detail = resolve(files)
    print("=== CLASS ONE (calibrated on the seven canon phrases) ===")
    tot = 0
    for num, rows in detail:
        print(num, "claims:", len(rows), [r[0] for r in rows])
        tot += len(rows)
    print("TOTAL class-one claims:", tot)
    print("MISMATCHES:", len(mism))
    for m in mism:
        print("   ", m)
    print()
    print("=== CLASS TWO ('in N words') ===")
    for num, lines in files:
        sp = speech_paragraphs(lines)
        for i, ln in enumerate(lines):
            s = ln.strip()
            if s.startswith(">") and s.strip('> ').strip().startswith("**") \
               and s.strip('> ').strip().endswith("**"):
                sp.append((i, s.strip('> ').strip()[2:-2]))
        sp.sort()
        c2 = class_two(lines)
        for i, n, txt in c2:
            tgt = next((b for k, b in sp if k > i), None)
            got = count_sentence_words(tgt) if tgt else -1
            print("   ch", num, "line", i + 1, "claim", n, "printed", got,
                  "REPRODUCES" if got == n else "MISMATCH")
    print("total class-two-shaped:",
          sum(len(class_two(lines)) for _, lines in files))
    print()
    print("=== DENOMINATOR (method per Batch 0005 section 7) ===")
    d = denom(files)
    print("denominator:", d)
    print("wc -w per chapter:")
    w, tot2 = wc(files)
    for n, v in w.items():
        print("  ", n, v)
    print("block wc -w total:", tot2)
    print()
    print("=== SHARED TWELVE-WORD RUNS (windows per line) ===")
    print(twelve_word_runs(files))
    print("=== IDENTICAL PARAGRAPHS >= 12 words ===")
    ip = identical_paragraphs(files)
    print(len(ip))
    for k, v in list(ip.items())[:10]:
        print("   ", v, k[:80])
    print()
    print("=== BOLD CLAUSES PER CHAPTER ===")
    for n, v in bold_clauses(files).items():
        print("  ", n, v)
    print()
    print("=== FOOTER SUPPORT ===")
    fs = footer_support(files)
    print("bad:", len(fs))
    for f in fs:
        print("   ", f)
    print()
    print("=== RESERVED TERMS ===")
    for k, v in reserved_scan(files).items():
        print("  ", k, v)
    print()
    print("=== FRAME TABLE (literal strings, whole-word) ===")
    FRAMES = ["clerk", "clerk of nineteen years", "A clerk of nineteen years entered",
              "the clerk entered that", "mends fencing", "digs loam", "man of fifty-six",
              "a lock", "a toll", "a notice", "a chair", "a page", "a column",
              "a charter", "a covenant", "a slate", "a wall", "a party", "a house",
              "a gate", "and a man of fifty-six", "in the six things",
              "in front of about nineteen people", "which is the rule of the counter",
              "gave the figures", "a man of about nineteen counted it and got",
              "it went in the minute in his own words", "not asked",
              "Lot Seventeen", "a stranger can walk up to", "a name put on a figure",
              "nobody owns the water", "a bell", "a second book", "a figure",
              "a ditch", "a rope", "a keeper", "four hundred and eleven",
              "the month before last", "last month"]
    d = denom(files)
    blob = []
    for num, lines in files:
        blob.append((num, "\n".join(lines).lower()))
    for f in FRAMES:
        c = 0
        for num, txt in blob:
            c += len(re.findall(r"(?<![a-z-])" + re.escape(f.lower()) + r"(?![a-z-])", txt))
        rate = ("1/%d" % round(d / c)) if c else "-"
        print("   %-52s %5d  %s" % (f, c, rate))
    print()
    print("=== MARKDOWN / UNIT / WEEKDAY INTEGRITY ===")
    ig = integrity(files)
    print("issues:", len(ig))
    for i in ig:
        print("   ", i)


if __name__ == "__main__":
    main()

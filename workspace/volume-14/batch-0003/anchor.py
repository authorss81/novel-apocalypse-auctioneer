#!/usr/bin/env python3
"""Validate the resolver and run the anchor test.

Validation: on a chapter that is NOT this block's and was not edited, the
resolver must return the same integers as the whitespace word counts of the
bolded speeches, against the figures the pages claim.
"""
import re
import sys
sys.path.insert(0, '/tmp/opencode')
from resolver import resolve

SPEECH = re.compile(r'^\"\*\*(.+)\*\*\"$')
CLAIM = re.compile(r'and the boy counted what \w+ said and got ([a-z\- ]+?) and read the number back')


def speeches_and_claims(path):
    with open(path, encoding='utf-8') as fh:
        lines = fh.read().split('\n')
    out = []
    for i, line in enumerate(lines):
        m = CLAIM.search(line)
        if not m:
            continue
        for j in range(i + 1, len(lines)):
            sm = SPEECH.match(lines[j].strip())
            if sm:
                out.append((m.group(1), sm.group(1)))
                break
    return out


def validate(path, expect):
    ok = True
    got = []
    for claimed, body in speeches_and_claims(path):
        n = resolve(claimed)
        w = len(body.split())
        r = n[0][0] if n else None
        got.append((r, w))
        if r != w:
            ok = False
    print(path.rsplit('/', 1)[-1], 'resolved vs speech words:', got)
    if expect:
        print('  expected:', expect, '->',
              'PASS' if [g[0] for g in got] == expect else 'FAIL')
        ok = ok and [g[0] for g in got] == expect
    return ok


# ---- the eighteen carrier phrases, in the form this house writes them ----
# (row, the phrase as it stands on the page, the direction the figure lies,
#  the expected figure as a function of c, or None for the constant)
CARRIERS = [
    (1, 'the board carries', 'fwd', 0, lambda c: 548 + c),
    (2, 'the train on that siding has stood', 'fwd', 0, lambda c: 864 + c),
    (3, 'nobody has entered anything for', 'fwd', 0, lambda c: 578 + c),
    (4, 'days separate the second of January and this morning', 'bwd', 1, lambda c: 539 + c),
    (5, 'days is how long the bid has been open', 'bwd', 1, lambda c: 298 + c),
    (6, 'printed nights is', 'fwd', 0, lambda c: 431 + c),
    (7, 'days is how far behind the figure on the second line', 'bwd', 1, lambda c: 253 + c),
    (8, 'days is how long the rule said out loud in that yard has stood', 'bwd', 1, lambda c: 258 + c),
    (9, 'days is how long it has been since the first day of the eighth month', 'bwd', 1, lambda c: 328 + c),
    (10, 'days past a printing it did not make', 'bwd', 1, lambda c: 267 + c),
    (11, 'days as the age of that figure', 'bwd', 1, lambda c: 389 + c),
    (12, 'the figure on the sheet at that gatepost is', 'fwd', 0, None),
    (13, 'night of that run', 'bwd', 1, lambda c: 289 + c, 'last'),
    (14, 'he has slept on', 'fwd', 0, lambda c: 288 + c),
    (15, 'marks have been cut off that board', 'bwd', 1, lambda c: 207 + c),
    (16, 'marks in chalk along the edge of that second table', 'bwd', 1, lambda c: 193 + c, 'last'),
    (17, 'of those mornings', 'bwd', 1, lambda c: 375 + c, 'last'),
    (18, 'the copy at the near end of them has now been on that wood for', 'fwd', 1, lambda c: 148 + c),
]


def run_before(text, idx, skip=0):
    """The maximal numeric run abutting position idx, scanning leftwards.

    `skip` counts trailing non-numeric tokens between the phrase and the run,
    which in this manuscript is the unit noun (`days`, `marks`, `night`).
    """
    from resolver import is_numtok
    toks = re.findall(r'[a-zA-Z\-]+', text[:idx])
    i = len(toks) - 1
    while skip > 0 and i >= 0 and not is_numtok(toks[i].casefold()):
        i -= 1
        skip -= 1
    run = []
    while i >= 0:
        t = toks[i].casefold()
        if is_numtok(t) and t != 'and':
            run.insert(0, t)
        elif t == 'and' and i - 1 >= 0 and toks[i - 1].casefold() in ('hundred', 'thousand'):
            run.insert(0, t)
        else:
            break
        i -= 1
    return ' '.join(run)

def run_after(text, idx, skip=0):
    """The maximal numeric run abutting position idx, scanning rightwards."""
    from resolver import is_numtok
    toks = re.findall(r'[a-zA-Z\-]+', text[idx:])
    i = 0
    while skip > 0 and i < len(toks) and not is_numtok(toks[i].casefold()):
        i += 1
        skip -= 1
    run = []
    while i < len(toks):
        t = toks[i].casefold()
        if is_numtok(t) and t != 'and':
            run.append(t)
        elif t == 'and' and run and run[-1] in ('hundred', 'thousand'):
            run.append(t)
        else:
            break
        i += 1
    return ' '.join(run)


def anchor(path, c):
    with open(path, encoding='utf-8') as fh:
        text = fh.read()
    text = re.sub(r'[ \t]+', ' ', text)
    found = 0
    rows = []
    for row in CARRIERS:
        n, phrase, direction, skip, want = row[:5]
        which = row[5] if len(row) > 5 else 'first'
        if n == 18 and c >= 36:
            rows.append((n, phrase, None, 'STOPPED', 'STOPPED on day 36, the table is not in that yard'))
            continue
        hay = text.casefold()
        idx = hay.rfind(phrase.casefold()) if which == 'last' else hay.find(phrase.casefold())
        if idx < 0:
            rows.append((n, phrase, None, want(c) if want else 411, 'ABSENT'))
            continue
        run = run_after(text, idx + len(phrase), skip) if direction == 'fwd' \
            else run_before(text, idx, skip)
        r = resolve(run)
        got = r[0][0] if r else None
        exp = 411 if want is None else want(c)
        if n == 18 and c >= 36:
            # row 18 stops on day 35
            rows.append((n, phrase, got, exp, 'STOPPED' if got is None else 'STILL PRINTED'))
            continue
        rows.append((n, phrase, got, exp, 'ok' if got == exp else 'FAIL'))
        if got == exp:
            found += 1
    return found, rows


if __name__ == '__main__':
    v = validate('chapters/volume-13/chapter-0640.md', [143, 129, 164])
    print('resolver validation on Ch 640:', 'PASS' if v else 'FAIL')
    print()
    for path, c in [('chapters/volume-14/chapter-0681.md', 31)]:
        f, rows = anchor(path, c)
        for n, ph, got, exp, st in rows:
            print('%2d %-70s got=%-8s expected=%-8s %s' % (n, ph[:70], got, exp, st))
        print('ANCHOR: %d of 18 in their own carrier phrases' % f)

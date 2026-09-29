#!/usr/bin/env python3
"""Word-number resolver, lifted in behaviour from state/volume-13-close.md.

Five named defects are carried, plus the sixth this phase found:
 1. case fold before tokenising
 2. `and` consumable inside a number only after `hundred`/`thousand`, AND a
    maximal numeric run is split at a non-consumable `and`
 3. hyphenated token contributes tens + units at one step
 4. zero is kept
 5. a hundreds parser adds `one hundred and six` as 106
 6. ordinal words are looked up EXACTLY before any suffix stripping
"""
import re

ONES = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11,
        'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
        'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19}
TENS = {'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60,
        'seventy': 70, 'eighty': 80, 'ninety': 90}
ORDINAL = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4, 'fifth': 5,
           'sixth': 6, 'seventh': 7, 'eighth': 8, 'ninth': 9, 'tenth': 10,
           'eleventh': 11, 'twelfth': 12, 'thirteenth': 13, 'fourteenth': 14,
           'fifteenth': 15, 'sixteenth': 16, 'seventeenth': 17,
           'eighteenth': 18, 'nineteenth': 19, 'twentieth': 20,
           'thirtieth': 30, 'fortieth': 40, 'fiftieth': 50, 'sixtieth': 60,
           'seventieth': 70, 'eightieth': 80, 'ninetieth': 90,
           'hundredth': 100, 'thousandth': 1000}
SCALES = {'hundred': 100, 'thousand': 1000}
WORDNUM = set(ONES) | set(TENS) | set(ORDINAL) | set(SCALES) | {'and'}


def _simple(tok):
    """Value of one non-hyphenated token, or None."""
    if tok in ONES:
        return ONES[tok]
    if tok in TENS:
        return TENS[tok]
    if tok in ORDINAL:
        return ORDINAL[tok]
    if tok in SCALES:
        return SCALES[tok]
    return None


def _compound(tok):
    """A hyphenated token contributes tens plus units at one step."""
    parts = tok.split('-')
    if len(parts) == 2 and parts[0] in TENS:
        if parts[1] in ONES:
            return TENS[parts[0]] + ONES[parts[1]]
        if parts[1] in ORDINAL and 1 <= ORDINAL[parts[1]] <= 19:
            return TENS[parts[0]] + ORDINAL[parts[1]]
    return None


def run_value(tokens):
    """Value of a maximal run of number words already known to be contiguous."""
    total = 0
    current = 0
    seen = False
    for tok in tokens:
        if tok == 'and':
            continue
        v = _compound(tok)
        if v is None:
            v = _simple(tok)
        if v is None:
            return None
        if v == 100:
            # a round-hundred ordinal in a run is a MULTIPLIER, not a sum
            current = (current if current else 1) * 100
            seen = True
            continue
        if v == 1000:
            current = (current if current else 1) * 1000
            seen = True
            continue
        if v >= 20 and v < 100:
            current += v
        else:
            current += v
        seen = True
    total += current
    return total if seen else None


def is_numtok(tok):
    return tok in WORDNUM or _compound(tok) is not None


def resolve(text):
    """Every number in `text`, in reading order."""
    toks = re.findall(r"[a-z\-]+", text.casefold())
    out = []
    i = 0
    while i < len(toks):
        if is_numtok(toks[i]) and toks[i] != 'and':
            j = i
            run = []
            while j < len(toks):
                t = toks[j]
                if t == 'and':
                    # consumable inside a number only after hundred/thousand
                    if run and run[-1] in ('hundred', 'thousand'):
                        run.append(t)
                        j += 1
                        continue
                    break
                if is_numtok(t):
                    run.append(t)
                    j += 1
                else:
                    break
            v = run_value(run)
            if v is not None:
                out.append((v, ' '.join(run)))
            i = j
        else:
            i += 1
    return out


if __name__ == '__main__':
    for s in ['five hundred and eighty-four', 'three hundred and twenty-fifth',
              'the four hundredth of those mornings', 'three hundred and '
              'thirty-fifth', 'the two hundred and eighty-ninth',
              'four hundred and eleven', 'eight hundred and thirty',
              'one hundred and six', 'about nine inches']:
        print(s, '->', resolve(s))

"""
https://www.hackerrank.com/challenges/happy-ladybugs/problem?isFullScreen=true
"""

from collections import Counter


def happyLadybugs(b):
    counter = Counter(b)
    if not all([False if v == 1 and k != "_" else True for k, v in counter.items()]):
        return "NO"
    if counter["_"] >= 1:
        return "YES"
    l, r = 0, 0
    happy = 0
    while r < len(b):
        if b[l] == b[r]:
            happy += 1

        else:
            if happy == 0:
                return "NO"
            l = r
            happy = 0
        r += 1
    return "YES"

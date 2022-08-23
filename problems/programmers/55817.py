"""
https://school.programmers.co.kr/learn/courses/9899/lessons/55817?language=python3
"""

from collections import Counter


def solution1(participant, completion):
    p_cnt = Counter(participant)
    c_cnt = Counter(completion)
    diff = p_cnt - c_cnt
    return list(diff.keys())[0]


def solution2(participant, completion):
    hash_map = {}
    people = 0

    for part in participant:
        val = hash(part)
        people += val
        hash_map[val] = part
    for comp in completion:
        val = hash(comp)
        people -= val

    return hash_map[people]

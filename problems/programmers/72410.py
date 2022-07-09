"""
https://school.programmers.co.kr/learn/courses/30/lessons/72410
"""

import re
import copy


def solution(new_id):
    answer = copy.copy(new_id)
    # 1
    answer = answer.lower()
    # 2
    not_allow_char = re.compile(r"[^a-z\-_.0-9]")
    answer = re.sub(not_allow_char, "", answer)
    # 3
    answer = re.sub("\.{2,}", ".", answer)
    # 4
    if len(answer) > 0:
        if answer[0] == ".":
            answer = answer[1:]
    if len(answer) > 0:
        if answer[-1] == ".":
            answer = answer[:-1]
    # 5
    if not answer:
        answer = "a"
    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
    # 7
    if len(answer) <= 2:
        answer += answer[-1] * (3 - len(answer))
    return answer

"""
https://school.programmers.co.kr/learn/courses/30/lessons/76501
"""


def solution(absolutes, signs):
    ret = 0
    for absolute, sign in zip(absolutes, signs):
        if sign:
            ret += absolute
        else:
            ret -= absolute

    return ret

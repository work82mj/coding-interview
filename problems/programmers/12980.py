"""
https://programmers.co.kr/learn/courses/30/lessons/12980
"""


def solution(n):
    ret = 0
    while n != 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n -= 1
            ret += 1
    return ret

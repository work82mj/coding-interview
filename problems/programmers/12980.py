"""
https://programmers.co.kr/learn/courses/30/lessons/12980
"""


def solution2(n):
    return bin(n).count("1")


def solution1(n):
    ret = 0
    while n != 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n -= 1
            ret += 1
    return ret

"""
https://school.programmers.co.kr/learn/courses/9899/lessons/55825
"""


def solution(numbers):
    strings = sorted(list(map(str, numbers)), key=lambda x: x * 3, reverse=True)
    num = int("".join(strings))
    return str(num)

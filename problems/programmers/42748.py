"""
https://school.programmers.co.kr/learn/courses/30/lessons/42748
"""


def solution1(array, commands):
    rets = []
    for command in commands:
        i, j, k = command
        rets.append(sorted(array[i - 1 : j])[k - 1])
    return rets


def solution2(array, commands):
    return [
        sorted(array[command[0] - 1 : command[1]])[command[2] - 1]
        for command in commands
    ]

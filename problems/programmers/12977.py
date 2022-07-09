"""
https://school.programmers.co.kr/learn/courses/30/lessons/12977
"""


def solution(nums):
    ret = 0
    primes = [False, False] + [True] * 3000
    for i in range(2, int(3000 ** 0.5)):
        if primes[i]:
            for ii in range(2 * i, 3000, i):
                primes[ii] = False
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if primes[nums[i] + nums[j] + nums[k]]:
                    ret += 1

    return ret

"""
https://app.codility.com/demo/results/trainingUX5C3G-6RK/
"""


def solution(A, B, K):
    upper = B // K
    lower = A // K

    ret = upper - lower

    if A % K == 0:
        ret += 1

    return ret

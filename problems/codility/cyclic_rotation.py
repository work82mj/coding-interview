"""
https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
"""


def solution(A, K):
    if len(A) == 0:
        return A

    num = K % len(A)
    return A[-num:] + A[:-num]

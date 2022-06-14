"""
https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/
"""


def solution(A):
    ret = 0

    if not A:
        return -1

    passing = 0
    for i in range(len(A) - 1, -1, -1):
        if A[i] == 1:
            passing += 1
        else:
            ret += passing

    # check limits
    if ret > 1000000000:
        return -1

    return ret

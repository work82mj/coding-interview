"""
https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
"""


def solution(A):
    sorted_arr = sorted(A)

    ret = 1

    for x in sorted_arr:
        if x > ret:
            return ret
        ret += 1
    return ret

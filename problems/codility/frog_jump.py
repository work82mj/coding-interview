"""
https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
"""

from math import ceil


def solution(X, Y, D):
    return ceil((Y - X) / D)

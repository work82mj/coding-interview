"""
https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
"""


def solution(N):
    # write your code in Python 3.6

    binary_string = str(bin(N))[2:]

    max_gap = 0
    gap = 0

    for s in binary_string:
        if s == "1":
            max_gap = max(max_gap, gap)
            gap = 0
        else:
            gap += 1

    return max_gap

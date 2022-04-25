"""
https://www.hackerrank.com/challenges/icecream-parlor/problem?isFullScreen=true
"""


def icecreamParlor(m, arr):
    for i, cost in enumerate(arr):
        if m - cost in arr:
            if arr.index(m - cost) != i:
                return sorted([i + 1, arr.index(m - cost) + 1])

"""
https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
"""
from collections import Counter


def solution(A):
    counter = Counter(A)
    for key, val in counter.items():
        if val % 2 != 0:
            return key

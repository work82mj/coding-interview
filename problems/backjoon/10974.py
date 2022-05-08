"""
https://www.acmicpc.net/problem/10974

input1
3

output1
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""

import sys
import itertools

sys.stdin = open("problems/backjoon/input.txt", "r")
N = int(sys.stdin.readline())
numbers = list(range(N+1))[1:]

for item in itertools.permutations(numbers):
    perm = [str(num) for num in list(item)]
    print(" ".join(perm))
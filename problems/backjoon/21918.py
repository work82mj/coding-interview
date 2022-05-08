"""
https://www.acmicpc.net/problem/21918

input1
8 3
0 0 0 0 0 0 0 0
1 2 1
1 4 1
2 2 4

output1
0 0 1 0 0 0 0 0

input2
8 6
0 0 0 0 0 0 0 0
1 2 1
1 4 1
2 2 4
2 1 7
3 5 8
4 4 6

output2
1 1 0 1 1 1 0 0
"""

import sys

sys.stdin = open("problems/backjoon/input.txt", "r")
N, M = map(int, sys.stdin.readline().split(" "))
s = [0] + list(map(int, sys.stdin.readline().split(" ")))

for _ in range(M):
    command, i, j = map(int, sys.stdin.readline().split(" "))

    if command == 1:
        s[i] = j
    elif command == 2:
        for idx in range(i, j+1):
            if s[idx] == 0 :
                s[idx] = 1
            else:
                s[idx] = 0
    elif command == 3:
        s[i: j + 1] = [0] * (j + 1 - i)
    elif command == 4:
        s[i: j + 1] = [1] * (j + 1 - i)


print(" ".join(list(map(str, s[1:]))))
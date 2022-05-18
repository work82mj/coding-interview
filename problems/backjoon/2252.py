"""
https://www.acmicpc.net/problem/2252

input1:
3 2
1 3
2 3

output1:
1 2 3

input2:
4 2
4 2
3 1

output2:
4 2 3 1

"""

import sys
from collections import deque

sys.stdin = open("problems/backjoon/input.txt", "r")


def topology_sort():
    ret = []
    q = deque()
    for i in range(1, N + 1):
        if in_degrees[i] == 0:
            q.append(i)
    while q:
        curr = q.popleft()
        ret.append(curr)
        for nxt in graphs[curr]:
            in_degrees[nxt] -= 1
            if in_degrees[nxt] == 0:
                q.append(nxt)
    return ret


N, M = map(int, sys.stdin.readline().split())

graphs = [[] for _ in range(N + 1)]
in_degrees = [0 for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graphs[a].append(b)
    in_degrees[b] += 1

ret = topology_sort()

print(" ".join(list(map(str, ret))))

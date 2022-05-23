"""
https://www.acmicpc.net/problem/1766

input1:
4 2
4 2
3 1

output1:
3 1 4 2
"""

import sys
import heapq

sys.stdin = open("problems/backjoon/input.txt", "r")


def topology_sort():
    q = []
    for i in range(1, N + 1):
        if in_degrees[i] == 0:
            heapq.heappush(q, i)
    ret = []
    while q:
        curr = heapq.heappop(q)
        ret.append(curr)
        for nxt in graphs[curr]:
            in_degrees[nxt] -= 1
            if in_degrees[nxt] == 0:
                heapq.heappush(q, nxt)
    return ret


N, M = map(int, sys.stdin.readline().split())
graphs = [[] for _ in range(N + 1)]
in_degrees = [0 for _ in range(N + 1)]

for _ in range(M):
    easy, hard = map(int, sys.stdin.readline().split())
    graphs[easy].append(hard)
    in_degrees[hard] += 1

ret = topology_sort()

print(*ret)

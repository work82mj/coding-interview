"""
https://www.acmicpc.net/problem/1504

input1:
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3

output1:
7
"""

import sys
import heapq

sys.stdin = open("problems/backjoon/input.txt", "r")


def dijkstra(start):
    queue = []
    distances = [float("inf") for _ in range(N + 1)]
    heapq.heappush(queue, (0, start))
    distances[start] = 0

    while queue:
        curr_dist, curr = heapq.heappop(queue)
        if distances[curr] < curr_dist:
            continue
        for nxt, nxt_dist in enumerate(graphs[curr]):
            if nxt_dist and curr_dist + nxt_dist < distances[nxt]:
                distances[nxt] = curr_dist + nxt_dist
                heapq.heappush(queue, (curr_dist + nxt_dist, nxt))

    return distances


N, E = map(int, sys.stdin.readline().split())

graphs = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graphs[a][b] = c
    graphs[b][a] = c

v1, v2 = map(int, sys.stdin.readline().split())

start_distances = dijkstra(1)
v1_distances = dijkstra(v1)
v2_distances = dijkstra(v2)

ret = min(
    start_distances[v1] + v1_distances[v2] + v2_distances[N],
    start_distances[v2] + v2_distances[v1] + v1_distances[N],
)

print(ret if ret < float("inf") else -1)

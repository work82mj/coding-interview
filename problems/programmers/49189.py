"""
https://programmers.co.kr/learn/courses/30/lessons/49189
"""

import heapq
from collections import Counter

def solution(n, edge):
    def dijkstra(start):
        queue = []
        heapq.heappush(queue, (0, start))
        distances[start] = 0

        while queue:
            curr_dist, curr = heapq.heappop(queue)
            if distances[curr] < curr_dist:
                continue
            for nxt, nxt_dist in graphs[curr]:
                if nxt_dist and nxt_dist + curr_dist < distances[nxt]:
                    distances[nxt] = nxt_dist + curr_dist
                    heapq.heappush(queue, (nxt_dist + curr_dist, nxt))

    graphs = [[] for _ in range(n + 1)]
    distances = [float("inf") for _ in range(n + 1)]
    for vertex in edge:
        a, b = vertex
        graphs[a].append([b, 1])
        graphs[b].append([a, 1])

    dijkstra(1)

    counter = Counter(distances[1:])

    return counter[max(distances[1:])]

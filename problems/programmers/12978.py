"""
https://programmers.co.kr/learn/courses/30/lessons/12978
"""

import heapq


def solution(N, road, K):
    def dijkstra(start):
        queue = []
        heapq.heappush(queue, (0, start))
        distances[start] = 0

        while queue:
            dist, nxt = heapq.heappop(queue)
            if distances[nxt] < dist:
                continue
            for node, val in enumerate(graphs[nxt]):
                if val != float("inf"):
                    if dist + val < distances[node]:
                        distances[node] = dist + val
                        heapq.heappush(queue, (dist + val, node))

    graphs = [[float("inf")] * (N + 1) for _ in range(N + 1)]
    for info in road:
        a, b, c = info
        graphs[a][b] = min(graphs[a][b], c)
        graphs[b][a] = min(graphs[b][a], c)

    distances = [float("inf") for _ in range(N + 1)]

    dijkstra(1)

    count = 0
    for val in distances:
        if val <= K:
            count += 1
    return count

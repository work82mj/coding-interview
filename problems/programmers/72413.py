"""
https://programmers.co.kr/learn/courses/30/lessons/72413
"""

import heapq


def solution(n, s, a, b, fares):
    def dijkstra(start, distances):
        queue = []
        heapq.heappush(queue, (0, start))
        distances[start] = 0

        while queue:
            curr_dist, curr = heapq.heappop(queue)
            if distances[curr] < curr_dist:
                continue
            for nxt, nxt_dist in enumerate(graphs[curr]):
                if nxt_dist != float("inf"):
                    if nxt_dist + curr_dist < distances[nxt]:
                        distances[nxt] = nxt_dist + curr_dist
                        heapq.heappush(queue, (nxt_dist + curr_dist, nxt))
        return distances

    graphs = [[float("inf")] * (n + 1) for _ in range(n + 1)]
    for fare in fares:
        c, d, f = fare
        graphs[c][d] = f
        graphs[d][c] = f

    s_to_every = dijkstra(s, [float("inf") for _ in range(n + 1)])
    a_to_every = dijkstra(a, [float("inf") for _ in range(n + 1)])
    b_to_every = dijkstra(b, [float("inf") for _ in range(n + 1)])

    ret = a_to_every[s] + b_to_every[s]
    for i in range(n + 1):
        together = s_to_every[i] + a_to_every[i] + b_to_every[i]
        ret = min(ret, together)

    return ret

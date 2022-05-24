"""
https://www.acmicpc.net/problem/10282

input1:
2
3 2 2
2 1 5
3 2 5
3 3 1
2 1 2
3 1 8
3 2 4

output1:
2 5
3 6

Notice:
topology sort cannot consider other shorter paths to infect computers.
"""
import sys
import heapq

sys.stdin = open("problems/backjoon/input.txt", "r")


def dijkstra(start):
    queue = []
    sec_list = [float("INF") for _ in range(n + 1)]
    sec_list[start] = 0
    heapq.heappush(queue, [0, start])

    while queue:
        curr_sec, curr = heapq.heappop(queue)

        if sec_list[curr] < curr_sec:
            continue
        else:
            for nxt, nxt_sec in graph[curr]:
                if curr_sec + nxt_sec < sec_list[nxt]:
                    sec_list[nxt] = curr_sec + nxt_sec
                    heapq.heappush(queue, [curr_sec + nxt_sec, nxt])
    return sec_list


test_case = int(sys.stdin.readline())

for _ in range(test_case):
    n, d, c = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(n + 1)]
    in_degree = [0 for _ in range(n + 1)]

    for dependency in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b].append([a, s])
        in_degree[a] += 1
    ret = dijkstra(c)
    cnt, max_sec = 0, 0
    for sec in ret:
        if sec != float("INF"):
            cnt += 1
            max_sec = max(max_sec, sec)
    print(cnt, max_sec)

"""
https://programmers.co.kr/learn/courses/30/lessons/43162
"""

from collections import defaultdict

def solution(n, computers):
    net = defaultdict(list)

    for i in range(n):
        for j in range(n):
            if computers[i][j] and i != j:
                net[i].append(j)
                net[j].append(i)

    clusters = []
    queue = []
    visited = []
    for i in range(n):
        if i not in visited:
            queue.append(i)
            cluster = set()
            while queue:
                com = queue.pop()
                cluster.add(com)
                if com not in visited:
                    visited.append(com)
                    queue.extend(net[com])
            clusters.append(list(cluster))

    return len(clusters)

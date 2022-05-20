import sys
from collections import deque

sys.stdin = open("problems/backjoon/input.txt", "r")

test_num = int(sys.stdin.readline())

for _ in range(test_num):
    N = int(sys.stdin.readline())
    last_ranking = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())

    # make graphs
    graphs = [[] for _ in range(N + 1)]
    in_degrees = [0 for _ in range(N + 1)]
    for i in range(N):
        for j in range(i + 1, N):
            graphs[last_ranking[i]].append(last_ranking[j])
            in_degrees[last_ranking[j]] += 1

    for _ in range(m):
        new, last = map(int, sys.stdin.readline().split())
        if last in graphs[new]:
            graphs[new].remove(last)
            graphs[last].append(new)
            in_degrees[last] -= 1
            in_degrees[new] += 1

        elif new in graphs[last]:
            graphs[last].remove(new)
            graphs[new].append(last)
            in_degrees[new] -= 1
            in_degrees[last] += 1

    # topology sort
    ret = []
    q = deque()
    result = True

    for i in range(1, N + 1):
        if in_degrees[i] == 0:
            q.append(i)
    if not q:
        result = False

    while q:
        if len(q) > 1:
            result = False
            break

        curr = q.popleft()
        ret.append(curr)

        for nxt in graphs[curr]:
            in_degrees[nxt] -= 1
            if in_degrees[nxt] == 0:
                q.append(nxt)
            elif in_degrees[nxt] < 0:
                result = False
                break

    if not result or len(ret) < N:
        print("IMPOSSIBLE")
    else:
        print(*ret)

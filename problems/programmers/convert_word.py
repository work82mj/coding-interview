"""
https://programmers.co.kr/learn/courses/30/lessons/43163
"""
from collections import deque

def solution(begin, target, words):
    if target not in words: return 0

    queue = deque()
    queue.append([begin, 0])
    visited = []

    while queue:
        curr, count = queue.popleft()
        if curr == target:
            return count
        for i in range(len(words)):
            tmp = 0
            if words[i] not in visited:
                for j in range(len(curr)):
                    if curr[j] != words[i][j]:
                        tmp += 1
                if tmp == 1:
                    queue.append([words[i], count + 1])
                    visited.append(words[i])
    else:
        return 0
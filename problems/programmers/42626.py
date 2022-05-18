"""
https://programmers.co.kr/learn/courses/30/lessons/42626#

intput1
scoville: [1, 2, 3, 9, 10, 12]
K: 7

output1
2
"""

import heapq


def solution(scoville, K):
    ret = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        one = heapq.heappop(scoville)
        two = heapq.heappop(scoville)
        heapq.heappush(scoville, one + two * 2)
        ret += 1

    return ret

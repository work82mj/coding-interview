"""
https://programmers.co.kr/learn/courses/30/lessons/49993
"""


def solution(skill, skill_trees):
    ret = 0
    for tree in skill_trees:
        order = []
        for t in tree:
            if t not in skill:
                continue
            else:
                order.append(skill.index(t))

        if order == list(range(len(order))):
            ret += 1

    return ret

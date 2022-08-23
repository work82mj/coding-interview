"""
https://school.programmers.co.kr/learn/courses/9899/lessons/55821
"""

# there is one error case
def solution(n, lost, reserve):
    tmp = reserve.copy()
    ret = 0
    for l in lost:
        if l in tmp:
            ret += 1
            tmp.pop(tmp.index(l))
        elif l - 1 in tmp:
            ret += 1
            tmp.pop(tmp.index(l - 1))
        elif l + 1 in tmp:
            ret += 1
            tmp.pop(tmp.index(l + 1))

    return n - len(lost) + ret

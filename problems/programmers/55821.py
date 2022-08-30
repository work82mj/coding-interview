"""
https://school.programmers.co.kr/learn/courses/9899/lessons/55821
"""

# there is one error case
def solution1(n, lost, reserve):
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

def solution2(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    ret = 0
    for i in set_reserve:
        if i - 1 in set_lost:
            set_lost.remove(i - 1)
        elif i + 1 in set_lost:
            set_lost.remove(i + 1)

    return n - len(set_lost)
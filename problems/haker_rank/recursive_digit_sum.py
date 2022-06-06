"""
https://www.hackerrank.com/challenges/recursive-digit-sum/problem?isFullScreen=true

input1:
148 3

output1:
3
"""


def superDigit(n, k):
    ret = 0
    for s in str(n):
        ret += int(s)
    ret *= k

    while ret >= 10:
        tmp_ret = 0
        for s in str(ret):
            tmp_ret += int(s)
        ret = tmp_ret
    return ret

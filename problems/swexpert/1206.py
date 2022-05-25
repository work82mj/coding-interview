"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
"""
import sys

sys.stdin = open("problems/swexpert/input.txt", "r")

T = 10

for test_case in range(1, T + 1):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    ret = 0
    for i in range(2, N - 2):
        max_height = max(arr[i - 1], arr[i - 2], arr[i + 1], arr[i + 2])
        view = arr[i] - max_height
        if view > 0:
            ret += view

    print(f"#{test_case} {ret}")

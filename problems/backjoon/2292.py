import sys

sys.stdin = open("problems/backjoon/input.txt", "r")
target = int(sys.stdin.readline())

if target == 1:
    print(1)
else:
    d1, d2 = 0, 0
    for i in range(1000000001):
        d1 += i
        d2 += i + 1
        min_v = 6 * d1 + 2
        max_v = 6 * d2 + 1

        if min_v <= target and target <= max_v:
            print(i + 2)
            break

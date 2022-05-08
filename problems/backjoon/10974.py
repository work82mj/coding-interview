import sys
import itertools

sys.stdin = open("problems/backjoon/input.txt", "r")
N = int(sys.stdin.readline())
numbers = list(range(N+1))[1:]

for item in itertools.permutations(numbers):
    perm = [str(num) for num in list(item)]
    print(" ".join(perm))
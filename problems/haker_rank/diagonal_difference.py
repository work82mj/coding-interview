"""
https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true
"""


# O(N**2)
def diagonalDifference(arr):
    # Write your code here
    l2r, r2l = 0, 0

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                l2r += arr[i][j]
            if i + j == len(arr) - 1:
                r2l += arr[i][j]

    return abs(l2r - r2l)

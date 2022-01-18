"""
https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1168/

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        min_x, min_y = 0, 0
        max_x, max_y = len(matrix) - 1, len(matrix[0]) - 1

        ret = []

        while min_x < max_x and min_y < max_y:

            # right
            for y in range(min_y, max_y + 1):
                ret.append(matrix[min_x][y])
            min_x += 1

            # down
            for x in range(min_x, max_x + 1):
                ret.append(matrix[x][max_y])
            max_y -= 1

            # left
            for y in range(max_y, min_y - 1, -1):
                ret.append(matrix[max_x][y])
            max_x -= 1

            # up
            for x in range(max_x, min_x - 1, -1):
                ret.append(matrix[x][min_y])
            min_y += 1

        # inside
        if len(ret) < len(matrix) * len(matrix[0]):
            for x in range(min_x, max_x + 1):
                for y in range(min_y, max_y + 1):
                    ret.append(matrix[x][y])

        return ret

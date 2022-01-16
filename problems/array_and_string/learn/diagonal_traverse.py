"""
https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1167/

Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 10**4
1 <= m * n <= 10**4
-10**5 <= mat[i][j] <= 10**5
"""

from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        groups = defaultdict(list)
        for start, x in enumerate(range(len(mat))):
            for group, y in enumerate(range(len(mat[0]))):
                groups[start + group].append(mat[x][y])

        ret = []
        for group in groups.keys():
            nums = groups[group]
            if group % 2 == 0:
                nums.reverse()
                ret.extend(nums)
            else:
                ret.extend(nums)
        return ret

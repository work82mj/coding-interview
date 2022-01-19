"""
https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1170/

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:
1 <= numRows <= 30
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        ret = [[1]]
        for row_id in range(1, numRows):
            tmp = []
            for i in range(row_id + 1):
                if i == 0 or i == row_id:
                    tmp.append(1)
                else:
                    tmp.append(ret[row_id - 1][i - 1] + ret[row_id - 1][i])
            ret.append(tmp)
        return ret

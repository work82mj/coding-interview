"""
https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1171/

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]

Constraints:
0 <= rowIndex <= 33

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
"""


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        prev = [1, 1]

        for _ in range(2, rowIndex + 1):
            ret = [1]
            curr, nxt = 0, 1
            while nxt < len(prev):
                ret.append(prev[curr] + prev[nxt])
                curr, nxt = nxt, nxt + 1
            ret.append(1)
            prev = ret

        return prev
"""
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1154/

Given an integer array nums of 2n integers,
group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized.
Return the maximized sum.

Example 1:
Input: nums = [1,4,3,2]
Output: 4

Example 2:
Input: nums = [6,2,6,5,1,2]
Output: 9

Constraints:
1 <= n <= 104
nums.length == 2 * n
-104 <= nums[i] <= 104
"""


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        sums = 0

        for i in range(0, len(sorted_nums), 2):
            sums += min(sorted_nums[i], sorted_nums[i + 1])

        return sums

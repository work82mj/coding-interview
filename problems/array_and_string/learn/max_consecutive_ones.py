"""
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1301/

Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count, count = 0, 0

        for n in nums:
            if n == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0

        return max(max_count, count)

"""
https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/

You are given an integer array nums where the largest integer is unique.
Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

Example 1:
Input: nums = [3,6,1,0]
Output: 1

Example 2:
Input: nums = [1,2,3,4]
Output: -1

Example 3:
Input: nums = [1]
Output: 0

Constraints:

1 <= nums.length <= 50
0 <= nums[i] <= 100
The largest element in nums is unique.
"""


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        largest = max(nums)

        for idx, num in enumerate(nums):
            if largest != num:
                if num * 2 > largest:
                    return -1
        else:
            return nums.index(largest)
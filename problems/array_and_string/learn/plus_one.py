"""
https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1148/

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]

Example 3:
Input: digits = [9]
Output: [1,0]

Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num, length = 0, len(digits) - 1
        for idx, digit in enumerate(digits):
            num += digit * (10 ** (length - idx))

        string = str(num + 1)

        return [s for s in string]

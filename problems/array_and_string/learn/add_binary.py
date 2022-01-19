"""
https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1160/

Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_id, b_id = len(a) - 1, len(b) - 1
        ret, carry = [], 0

        while a_id >= 0 or b_id >= 0 or carry:
            if a_id >= 0:
                aa = int(a[a_id])
            else:
                aa = 0

            if b_id >= 0:
                bb = int(b[b_id])
            else:
                bb = 0

            curr = (aa + bb + carry) % 2
            carry = (aa + bb + carry) // 2

            ret.append(curr)

            a_id -= 1
            b_id -= 1

        return "".join([str(r) for r in ret[::-1]])

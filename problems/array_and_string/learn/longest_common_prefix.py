"""
https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1162/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pivot = min(strs, key=len)
        prefix = ""
        for s in pivot:
            for string in strs:
                if not string.startswith(prefix + s):
                    return prefix
            prefix += s

        return prefix

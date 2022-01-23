"""
https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1161/

Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Example 3:
Input: haystack = "", needle = ""
Output: 0

Constraints:
0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.
"""


class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        try:
            ret = haystack.index(needle)
            return ret
        except ValueError:
            return -1


class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


class Solution3:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        length = len(needle)
        for idx in range(len(haystack)):
            if haystack[idx : idx + length] == needle:
                return idx
        return -1

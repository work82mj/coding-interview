"""
https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1164/

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"

Example 3:
Input: s = "a good   example"
Output: "example good a"

Constraints:
1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
"""


class Solution1:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split(" ")
        ret = [word for word in words[::-1] if word]

        return " ".join(ret)


# Solution2 is faster than Solution1
class Solution2:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split(" ")

        ret = [word for word in words if word]
        ret.reverse()

        return " ".join(ret)

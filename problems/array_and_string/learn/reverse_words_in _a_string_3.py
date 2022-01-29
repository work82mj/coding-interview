"""
https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1165/

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "God Ding"
Output: "doG gniD"

Constraints:
1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""

class Solution1:
    def reverseWords(self, s: str) -> str:
        words = [word[::-1] for word in s.split()]
        return " ".join(words)

# two-pointer technique
class Solution2:
    def reverseWords(self, s: str) -> str:
        slow, fast = 0, 0
        ret = ''

        for idx, string in enumerate(s):
            if string == " ":
                ret += s[slow:fast][::-1]
                ret += " "
                slow = fast + 1

            fast += 1

        ret += s[slow:fast][::-1]

        return ret
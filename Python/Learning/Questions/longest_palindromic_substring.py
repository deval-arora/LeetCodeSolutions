"""
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

# Solution 1
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checkPalindrome(sub):
            lt, rt = 0, len(sub) - 1
            while lt < rt:
                if sub[lt] != sub[rt]:
                    return False
                lt += 1
                rt -= 1
            return True

        for window in range(len(s), 0, -1):
            for left in range(len(s)):
                right = window + left
                if right > len(s):
                    break
                if checkPalindrome(s[left: right]):
                    return s[left:right]

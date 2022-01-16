# https://leetcode.com/problems/repeated-substring-pattern/
# Example 1:

# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:

# Input: s = "aba"
# Output: false
# Example 3:

# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # print(len(s))
        for i in range(1, (len(s)//2 + 1)):
            if (s[:i] * (len(s) // len(s[:i]))) == s:
                return True
        return False

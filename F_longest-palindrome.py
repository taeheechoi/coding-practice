# https://leetcode.com/problems/longest-palindrome/
# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Example 3:

# Input: s = "bb"
# Output: 2


class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        
        count = Counter(s)
        result = 0
        oddExist = False
#         Counter({'c': 4, 'd': 2, 'a': 1, 'b': 1})
        for k, v in count.items():
            if v % 2 == 0:
                result += v
            else:
                if oddExist == False:
                    oddExist = True
                    result += v
                else:
                    result += v -1
        return result
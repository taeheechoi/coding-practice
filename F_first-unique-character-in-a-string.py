# https://leetcode.com/problems/first-unique-character-in-a-string/
# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        
        for k, v in Counter(s).items():
            if v == 1:
                return s.index(k)
        return -1
            
# https://leetcode.com/problems/ransom-note/
# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for r in ransomNote:
            if r in magazine:
                magazine = magazine.replace(r, '', 1)
            else:
                return False
        return True

#         d = {}
        
#         for m in magazine:
#             if m in d:
#                 d[m] += 1
#             else: 
#                 d[m] = 1
        
#         for r in ransomNote:
#             if r in d and d[r] > 0:
#                 d[r] -= 1
#             else:
#                 return False
            
#         return True
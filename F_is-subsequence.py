# https://leetcode.com/problems/is-subsequence/
# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # for i, x in enumerate(s):
        #     found_idx = 0
        #     for j, y in enumerate(t):
        #         if x == y and found_idx < j: 
        #             found_idx = j
        #         else:
        #             return False
        # return True
        p1 = 0
        p2 = 0
        
        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        return True if p1 == len(s) else False
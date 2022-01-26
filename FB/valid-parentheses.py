# https://leetcode.com/problems/valid-parentheses/
# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

class Solution:
    from collections import Counter
    def isValid(self, s: str) -> bool:
        r = []
        d = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in d.values():
                r.append(char)
            elif char in d.keys():
                if len(r) ==0: return False
                elif r.pop() != d[char]:
                    return False
        return len(r) == 0
            

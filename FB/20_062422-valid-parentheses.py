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
        stack = []
        d = {'(':')', '{': '}', '[':']'}
        for char in s:
            if char in d.keys():
                stack.append(d[char])
            elif char in d.values():
                if len(stack) == 0: return False
                if stack.pop() != char:
                    return False

        return len(stack) == 0
            



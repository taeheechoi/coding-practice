# https://leetcode.com/problems/valid-number/

# Example 1:

# Input: s = "0"
# Output: true
# Example 2:

# Input: s = "e"
# Output: false
# Example 3:

# Input: s = "."
# Output: false

import re
class Solution:
    
    def isNumber(self, s: str) -> bool:
        if re.match('^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$', s):
            return True
        else:
            return False
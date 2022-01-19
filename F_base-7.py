# https://leetcode.com/problems/base-7/
# Example 1:

# Input: num = 100
# Output: "202"
# Example 2:

# Input: num = -7
# Output: "-10"

class Solution:
    def convertToBase7(self, num: int) -> str:
        result = 0
        count = 0
        numAbs = abs(num)
        while numAbs > 0:
            result += (numAbs % 7) * 10**count
            numAbs //= 7
            count += 1
        
        return '-' +str(result) if num < 0 else str(result)            
        
            
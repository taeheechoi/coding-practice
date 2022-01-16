# https://leetcode.com/problems/add-strings/
# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"
# Example 2:

# Input: num1 = "456", num2 = "77"
# Output: "533"
# Example 3:

# Input: num1 = "0", num2 = "0"
# Output: "0"


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
#         s = {str(x):x for x in range(10)}
        
#         def strToInt(nums):
#             l = list(nums)
#             result = 0
#             for idx, num in enumerate(nums):
#                 result += s[num] * 10 ** (len(l)-1-idx)
#             return result
        
#         return str(strToInt(num1)+ strToInt(num2))
                
        s = {str(i):i for i in range(10)}
        
        def helper(num: str, ret: int = 0) -> int:
            for ch in num: 
                ret = ret * 10 + s[ch]
            return ret

        return str(helper(num1) + helper(num2))
# https://leetcode.com/problems/integer-to-english-words/

# Example 1:

# Input: num = 123
# Output: "One Hundred Twenty Three"
# Example 2:

# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:

# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"



# https://leetcode.com/problems/integer-to-english-words/discuss/528742/Python-3-Runtime-28ms-Recursive-approach
class Solution:
    def __init__(self):
        self.lessthan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def helper(self, num):
        if num == 0:
            return ""
        if num < 20:
            return self.lessthan20[num] + " "
        if num < 100:
            return self.tens[num//10] + " " + self.helper(num % 10)
        if num < 1000:
            return self.lessthan20[num // 100] + " Hundred " + self.helper(num%100)
    
    def numberToWords(self, num):
        if num == 0:
            return 'Zero'
        i = 0
        result = ''
        while num > 0:
            if num % 1000 > 0:
                result = self.helper(num%1000) + self.thousands[i] + ' ' + result
                num //= 1000
                i += 1
        return result


test = Solution()
# print(test.helper(52))
# print (123456789 // 1000)
print(test.numberToWords(1234567))

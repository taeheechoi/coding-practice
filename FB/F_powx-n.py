# https://leetcode.com/problems/powx-n/
# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

# Recursive
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n == 0:
#             return 1
#         if n < 0:
#             return 1 / self.myPow(x, abs(n))
#         return x * self.myPow(x, n - 1) if n % 2 else self.myPow(x * x, n // 2)
# Iterative
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         product, index = 1, abs(n)
#         while index:
#             if index % 2:
#                 product *= x
#             # accumulate base on the formula x ** 2n =  (x ** 2) ** n
#             x *= x  
#             index //= 2  # index always will be [1, 0] at last
#         return product if n >= 0 else 1 / product
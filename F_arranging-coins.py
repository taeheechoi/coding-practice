# https://leetcode.com/problems/arranging-coins/
# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.


# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.


class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
    
        while l <= r:
            m = (l + r) // 2
            target = m * (m +1) // 2
            if target == n:
                return m
            elif target < n:
                l = m + 1
            else:
                r = m - 1
        return r
    
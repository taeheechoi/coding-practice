# https://leetcode.com/problems/hamming-distance/
# https://dojang.io/mod/page/view.php?id=2460
# Example 1:

# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.
# Example 2:

# Input: x = 3, y = 1
# Output: 1

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        print(bin(x))
        print(bin(y))
        print(bin(x^y))
        return str(bin(x^y)).count('1')
 
        # return abs(len(bin(x)) - len(bin(y)))
        # value = str(bin(x^y))
        # return(value.count('1'))
        
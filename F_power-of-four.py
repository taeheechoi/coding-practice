# Example 1:

# Input: n = 16
# Output: true
# Example 2:

# Input: n = 5
# Output: false
# Example 3:

# Input: n = 1
# Output: true

def isPowerOfFour(self, n: int) -> bool:
    if n <=0: return False
    if n == 1: return True
    while n != 1:
        if n % 4 != 0: return False 
        n //= 4
    return True
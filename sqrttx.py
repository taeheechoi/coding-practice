# Example 1:

# Input: x = 4
# Output: 2
# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

def mySqrt(x):
    left, right = 0, x
    ans = 0
    while left <= right:
        mid = (left + right) // 2
       
        if mid*mid <= x:
            ans = mid
            left = mid+ 1
        else:
            right = mid -1
    return ans

print(mySqrt(8))



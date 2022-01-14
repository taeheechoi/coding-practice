# Example 1:

# Input: num = 16
# Output: true
# Example 2:

# Input: num = 14
# Output: false


def isPerfectSquare(self, num: int) -> bool:
    l = 1
    r = num
    while l <= r:
        m = (l + r) //2
        if m*m == num: return True
        elif m*m > num:
            r = m - 1
        else:
            l = m + 1
    return False
        
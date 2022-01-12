# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

def climbingStairs(n):
    if n <=2:
        return n
    x, y = 1, 2
    for _ in range(2, n):
        x, y = y, x + y
    return y
        

print(climbingStairs(5))
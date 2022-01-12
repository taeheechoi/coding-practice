# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

def containsNearbyDuplicate(nums):
    d = {}
    for i, v in enumerate(nums):
        if v in d and i - d[v] <= k:
            return True
        d[v] = i
    return False

# https://leetcode.com/problems/increasing-triplet-subsequence/

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:
n = 5
th1 = 5

n = 4
th1 = 4

n = 3
th1 = 3

n = 2
th1 = 2

n = 1
th1 = 1


# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
# n = 2
# th1 = 2

# n = 1
# th1 = 1

# n = 5
# th2 = 5

# n = 0
# th1 = 0

# n = 4
# th2 = 4

# n = 6
# True
# https://leetcode.com/problems/increasing-triplet-subsequence/discuss/78995/Python-Easy-O(n)-Solution


### two spaces to store low and high if all passed return True else False

def increasingTriple(nums):
    first = second = float('inf')

    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False
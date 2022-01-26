# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23

def maxSubarray(nums):
    maxSub = nums[0]
    curSum = 0

    for num in nums:
        if curSum < 0:
            curSum = 0
        curSum += num
        maxSub = max(maxSub, curSum)
    return maxSub     

print(maxSubarray([-2,1,-3,4,-1,2,1,-5,4]))


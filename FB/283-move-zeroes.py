# https://leetcode.com/problems/move-zeroes/
# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]


# https://leetcode.com/problems/move-zeroes/discuss/1748937/Python-Simple-and-Clean-Python-Solution-By-Two-Approach

# slow index to keep tracking next swap position, O(N)

def moveZeros(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
            j +=1
    print(nums)

nums = [0,1,0,3,12]
moveZeros(nums)
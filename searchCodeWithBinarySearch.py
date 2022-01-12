# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target < nums[mid]:
            right = mid - 1
        if target > nums[mid]:
            left = mid + 1
        if target == nums[mid]:
            return mid

print(searchInsert([1,3,5,6], 5))
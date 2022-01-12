# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


from typing import DefaultDict


# def twoSum(nums, target):
#     seen = {}
#     for idx, val in enumerate(nums):
#         other_num = target - val
#         if other_num in seen:
#             return[idx, seen[other_num]]
#         seen[val] = idx

def twoSum(nums, target):
    nums_seen = {}
    for idx, num in enumerate(nums):
        target_num = target - num
        if target_num in nums_seen:
            return [nums_seen[target_num], idx]
        nums_seen[num] = idx


print(twoSum([3,2,4], 6))
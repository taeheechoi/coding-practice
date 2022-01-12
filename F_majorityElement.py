# https://leetcode.com/problems/majority-element/
# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

def majorityElement(nums):
    result = {}

    for num in nums:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1

    for k, v in result.items():
        if v == max(result.values()):
            return k

print(majorityElement([3,2,2]))
    
    


# def majorityElement(self, nums: List[int]) -> int:
#   return max(set(nums), key = nums.count)
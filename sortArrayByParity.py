# https://leetcode.com/problems/sort-array-by-parity/
# Example 1:

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# Example 2:

# Input: nums = [0]
# Output: [0]    
    
def sortArrayByParity(nums):
    odd = []
    even = []
    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even + odd
    


sortArrayByParity([3,1,2,4])
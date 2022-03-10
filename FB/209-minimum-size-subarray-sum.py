# https://leetcode.com/problems/minimum-size-subarray-sum/
# https://leetcode.com/problems/minimum-size-subarray-sum/discuss/1774062/Python-Explanation-of-sliding-window-using-comments

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

# Time: O(n)
# Space: O(1)

def minSubArrayLen(target, nums):
    start = 0
    sum = 0
    min_size = float('inf')

    for i in range(len(nums)):
        sum += nums[i]
        while sum >= target:
            min_size = min(min_size, i - start + 1)
            sum -= nums[start]
            start += 1
    return min_size if min_size != float('inf') else 0



print(minSubArrayLen(7, [2,3,1,2,4,3]))
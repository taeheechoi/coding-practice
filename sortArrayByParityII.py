# https://leetcode.com/problems/sort-array-by-parity-ii/
# Example 1:

# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
# Example 2:

# Input: nums = [2,3]
# Output: [2,3]


def sortArrayByParityII(nums):
    odd = []
    even = []
    result = []
    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    print(odd, even)
    while len(odd) > 0:
        result.append(even.pop(0))
        result.append(odd.pop(0))

    return result

print(sortArrayByParityII([4,2,5,7]))

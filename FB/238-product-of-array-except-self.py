# https://leetcode.com/problems/product-of-array-except-self/

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# 




def productExceptSelf(nums):

    l_prod_list, r_prod_list = [], []
    l_prod, r_prod = 1, 1

    for num in nums:
        l_prod_list.append(l_prod)
        l_prod *= num

    for num in nums[::-1]:
        r_prod_list.append(r_prod)
        r_prod *= num

    return [x*y for x, y in zip(l_prod_list, r_prod_list[::-1])]


# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/discuss/1370348/Python-recursive-solution


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        
        mid = len(nums) // 2
        left = self.sortedArrayToBST(nums[0:mid])
        right = self.sortedArrayToBST(nums[mid + 1:])
        node = TreeNode(nums[mid], left, right)
        return node
        
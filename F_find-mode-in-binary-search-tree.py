# https://leetcode.com/problems/find-mode-in-binary-search-tree/
# Example 1:
# Input: root = [1,null,2,2]
# Output: [2]
# Example 2:

# Input: root = [0]
# Output: [0]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def inOrder(root):
            elements = []
            if not root:
                return []
            if root:
                elements += inOrder(root.left)
                elements.append(root.val)
                elements += inOrder(root.right)
            return elements
        
        from collections import Counter
        
        d = Counter(inOrder(root))
        l = d.most_common()

        occur = l[0][1]
        result = []
        for i in l:
            if i[1] == occur:
                result.append(i[0])
        return result
# https://leetcode.com/problems/symmetric-tree/
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Input: root = [1,2,2,null,3,null,3]
# Output: false













class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSymmetricBst(node1, node2):
            if node1 == None and node2 == None:
                return True
            elif node1 == None or node2 == None:
                return False
            else:
                return node1.val == node2.val and isSymmetricBst(node1.left, node2.right) and isSymmetricBst(node1.right, node2.left)
        if not root:
            return True
        
        return isSymmetricBst(root.left, root.right)
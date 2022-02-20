# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.

# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

# Input: root = [2,1], p = 2, q = 1
# Output: 2
        
### Understanding: just need to compare p, q val with root val because of BST


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if(p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        if(p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)

        return root
        
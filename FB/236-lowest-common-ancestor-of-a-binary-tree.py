# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/1627171/Simple-Python-recursive-solution

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/1752078/Python-oror-DFS-oror-Recursive-oror-Simple-oror-comments-added

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


# Input: root = [1,2], p = 1, q = 2
# Output: 1


### Understanding: Don't get confused with BST 235 quesiton. This is Binary Tree


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root: return None
        
        if p == root or q == root:
            return root

        left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        else:
            return left or right

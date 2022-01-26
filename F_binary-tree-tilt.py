# https://leetcode.com/problems/binary-tree-tilt/
# Input: root = [4,2,9,3,5,null,7]
# Output: 15
# Explanation: 
# Tilt of node 3 : |0-0| = 0 (no children)
# Tilt of node 5 : |0-0| = 0 (no children)
# Tilt of node 7 : |0-0| = 0 (no children)
# Tilt of node 2 : |3-5| = 2 (left subtree is just left child, so sum is 3; right subtree is just right child, so sum is 5)
# Tilt of node 9 : |0-7| = 7 (no left child, so sum is 0; right subtree is just right child, so sum is 7)
# Tilt of node 4 : |(3+5+2)-(9+7)| = |10-16| = 6 (left subtree values are 3, 5, and 2, which sums to 10; right subtree values are 9 and 7, which sums to 16)
# Sum of every tilt : 0 + 0 + 0 + 2 + 7 + 6 = 15
# Example 3:


# Input: root = [21,7,14,1,1,2,2,3,3]
# Output: 9
# https://leetcode.com/problems/binary-tree-tilt/discuss/1618442/Python-Solution%3A-97-faster-apply-depth-first-searching-recursive
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.tilt = 0
        def dfs(root):
            if root == None: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.tilt += abs(left - right)
            return root.val + left + right
        dfs(root)
        return self.tilt
        
        
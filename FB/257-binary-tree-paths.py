# https://leetcode.com/problems/binary-tree-paths/
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# Example 2:

# Input: root = [1]
# Output: ["1"]

class Solution:
    def binaryTreePath(self, root):
        elements = []

        def dfs(node, s):
            if not node: return
            if node.left is None and node.right is None:
                elements.append(s + str(root.val))
            s += str(node.val) + '->'
            dfs(root.left, s)
            dfs(root.right, s)
        dfs(root, '')

        return elements


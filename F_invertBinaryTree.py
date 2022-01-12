# https://leetcode.com/problems/invert-binary-tree/discuss/1669767/Invert-Binary-Tree-or-Python

def invertTree(root):
    if root:
        left = invertTree(root.left)
        right = invertTree(root.right)

        root.left, root.right = right, left
    return root
        
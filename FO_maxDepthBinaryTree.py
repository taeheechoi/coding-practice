# https://leetcode.com/problems/maximum-depth-of-binary-tree/


def maxDepth(root):
    if root == None:
        return 0

    else:
        depth = max(maxDepth(root.left), maxDepth(root.right))
        return 1 + depth





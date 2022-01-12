# https://leetcode.com/problems/maximum-depth-of-binary-tree/


def maxDepth(root):
  def minDepth(self, root: TreeNode) -> int:
    if not root:
        return 0  # return 0 as depth if empty tree
    elif not root.left and not root.right:
        return 1 # base case handling
    elif not root.left:
        return self.minDepth(root.right)+1 # if no left child then only path is right, so consider right depth
    elif not root.right:
        return self.minDepth(root.left)+1  # if no right child then only path is left, so consider left depth
    else:
        return min(self.minDepth(root.left), self.minDepth(root.right))+1 # if both child exist then pick the minimum one, add one for current node and return min depth
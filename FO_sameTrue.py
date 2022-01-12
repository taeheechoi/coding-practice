# https://leetcode.com/problems/same-tree/
# https://leetcode.com/problems/same-tree/discuss/1641647/Python-easy-dfs-solution
# https://leetcode.com/problems/same-tree/discuss/1297853/Explained-pythonpython3-solution
# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q: return True
    if not p or not q: return False
    print(p.val == q.val)
    if p.val != q.val: return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(5)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

print(isSameTree(p,q))


# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque()
        q.append(root)
        result = []
        while q:
            cur_level = []
            for _ in range(len(q)):
                cur_node = q.popleft()
                cur_level.append(cur_node.val)
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            result.append(cur_level)
        
        return result
https://leetcode.com/problems/binary-search-tree-iterator/discuss/1740297/Python3-deque

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.q = deque()
        
        def dfs(node):
            if node.left: dfs(node.left)
            self.q.append(node.val)
            if node.right: dfs(node.right)
        dfs(root)
        

    def next(self) -> int:
        return self.q.popleft()
        

    def hasNext(self) -> bool:
        return True if self.q else False


# https://leetcode.com/problems/binary-tree-right-side-view/discuss/1781611/Python-BFS-super-clean-and-easy-to-understand

def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        q = deque([root])
        ans = []
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if i == 0:
                    ans.append(node.val)
                if node.right: q.append(node.right)
                if node.left: q.append(node.left)
        return ans


deque([TreeNode{val: 1, left: TreeNode{val: 2, left: None, right: TreeNode{val: 5, left: None, right: None}}, right: TreeNode{val: 3, left: None, right: TreeNode{val: 4, left: None, right: None}}}])
deque([TreeNode{val: 1, left: TreeNode{val: 2, left: None, right: TreeNode{val: 5, left: None, right: None}}, right: TreeNode{val: 3, left: None, right: TreeNode{val: 4, left: None, right: None}}}])
deque([TreeNode{val: 1, left: TreeNode{val: 2, left: None, right: TreeNode{val: 5, left: None, right: None}}, right: TreeNode{val: 3, left: None, right: TreeNode{val: 4, left: None, right: None}}}])
deque([TreeNode{val: 1, left: TreeNode{val: 2, left: None, right: TreeNode{val: 5, left: None, right: None}}, right: TreeNode{val: 3, left: None, right: TreeNode{val: 4, left: None, right: None}}}])
deque([TreeNode{val: 1, left: TreeNode{val: 2, left: None, right: TreeNode{val: 5, left: None, right: None}}, right: TreeNode{val: 3, left: None, right: TreeNode{val: 4, left: None, right: None}}}])


TreeNode{val: 1, left: TreeNode{val: 2, left: None, right: TreeNode{val: 5, left: None, right: None}}, right: TreeNode{val: 3, left: None, right: TreeNode{val: 4, left: None, right: None}}}


deque([TreeNode{val: 1, left: TreeNode{val: 2, left: None, right: TreeNode{val: 5, left: None, right: None}}, right: TreeNode{val: 3, left: None, right: TreeNode{val: 4, left: None, right: None}}}])
deque([TreeNode{val: 3, left: None, right: TreeNode{val: 4, left: None, right: None}}, TreeNode{val: 2, left: None, right: TreeNode{val: 5, left: None, right: None}}])
deque([TreeNode{val: 4, left: None, right: None}, TreeNode{val: 5, left: None, right: None}])

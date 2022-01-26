from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(7)
root.left = TreeNode(-2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(15)
root.right = TreeNode(5)
root.right.left = TreeNode(8)
root.right.right = TreeNode(-1)


def treeLevelPrint(node):
    if root == None:
        return 
    q = deque()
    q.append(node)
    while 0 < len(q):        
        level_count = len(q)
        for _ in range(level_count):
            crnt_node = q.popleft()
            print(crnt_node.val, end= ' ')
            if crnt_node.left:
                q.append(crnt_node.left)
            if crnt_node.right:
                q.append(crnt_node.right)
        print('')

treeLevelPrint(root)


# https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/1672580/Easy-Python-Solution-for-InOrder-PreOrder-and-PostOrder-Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/1668348/Python-Solution-with-and-without-recursion


def inOrderTraversal(root):
    elements = []
    
    if root:
        elements += inOrderTraversal(root.left)
        elements.append(root.val)
        elements += inOrderTraversal(root.right)
        
    
    return elements
        


def preOrderTraversal(root):
    elements = []
    
    if root:
        elements.append(root.val)
        elements += inOrderTraversal(root.left)
        elements += inOrderTraversal(root.right)
        
    
    return elements

def postOrderTraversal(root):
    elements = []
    
    if root:
        elements += inOrderTraversal(root.left)
        elements += inOrderTraversal(root.right)
        elements.append(root.val)
        
    
    return elements
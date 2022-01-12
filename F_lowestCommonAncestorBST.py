def lowestCommonAncestor(root, p, q):
    if(p.val < root.val and q.val < root.val):
        return lowestCommonAncestor(root.left, p, q)
    if(p.val > root.val and q.val > root.val):
        return lowestCommonAncestor(root.right, p, q)

    return root
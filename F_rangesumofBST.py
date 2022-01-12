# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.


def rangeSumBST(root, low, high):
    res = 0
    if root:
        res = root.val if low <= root.val <= high else 0
        return res + rangeSumBST(root.lef, low, high) + rangeSumBST(root.right, low, high)
    return res
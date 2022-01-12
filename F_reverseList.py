
# https://leetcode.com/problems/reverse-linked-list/discuss/1630780/Python3-Short-and-Simple-or-In-place-O(1)-space-or-Iterative
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Input: head = [1,2]
# Output: [2,1]

# Input: head = []
# Output: []

def reverseList(head):
    prev = None
    while head:
        next = head.next
        head.next, prev = prev, head
        head = next
    return prev
# https://leetcode.com/problems/remove-linked-list-elements/
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# Example 2:

# Input: head = [], val = 1
# Output: []
# Example 3:

# Input: head = [7,7,7,7], val = 7
# Output: []


def removeElements(head, val):
    prev, curr = None, head
    while curr:
        if curr.val == val:
            if prev:
                prev.next = curr.next
            else: 
                head = curr.next
            curr = curr.next

        else:
            prev, curr = curr, curr.next
    return head



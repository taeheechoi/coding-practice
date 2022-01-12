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


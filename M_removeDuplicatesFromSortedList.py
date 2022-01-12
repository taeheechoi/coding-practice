# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]

# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

def removeDuplicatesFromSortedList(head):
    pointer = head
    while pointer and pointer.next:
        if pointer.next == pointer.val:
            pointer.next == pointer.next.next
        else:
            pointer = pointer.next
    return pointer

print(removeDuplicatesFromSortedList([1,1,2,3,3]))




# slow = head
# while slow and slow.next:
# 	if slow.next.val==slow.val:
# 		slow.next=slow.next.next
# 	else:
# 		slow = slow.next
# return head
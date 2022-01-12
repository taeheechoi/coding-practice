# https://leetcode.com/problems/palindrome-linked-list/
# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:

# Input: head = [1,2]
# Output: false


def isPalindrome(head):
    curr = head
    arr = [curr.val]
    while curr.next:
        curr = curr.next
        arr.append(curr.val)
    return arr == arr[::-1]


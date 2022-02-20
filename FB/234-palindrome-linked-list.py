# https://leetcode.com/problems/palindrome-linked-list/

# Input: head = [1,2,2,1]
# Output: true

# Input: head = [1,2]
# Output: false

### Understanding: while next exits, append all value to array and compare

class Solution:
    def isPalindrome(self, head):
        curr = head
        arr = []

        while curr:
            arr.append(curr.val)
            curr = curr.next

        return arr == arr[::-1]
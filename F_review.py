# https://leetcode.com/problems/reverse-only-letters/
# def reverseOnlyLetters(self, s: str) -> str:
#     left, right = 0, len(s) - 1
#     l = list(s)

#     while left < right:
#         if not l[left].isalpha():
#             left +=1
#             continue
#         if not l[right].isalpha():
#             right -=1
#             continue

#         l[left], l[right] = l[right], l[left]
#         left, right = left+1, right -1
#     return ''.join(l)

# https://leetcode.com/problems/power-of-three/
# def isPowerOfThree(self, n: int) -> bool:
#     if n == 0: return False
#     while n != 1:
#         if n % 3 != 0:
#             return False
#         n //= 3
#     return True
        


# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#     if(p.val < root.val and q.val < root.val):
#         return self.lowestCommonAncestor(root.left, p, q)
#     if(p.val > root.val and q.val > root.val):
#         return self.lowestCommonAncestor(root.right, p, q)

#     return root

# https://leetcode.com/problems/reverse-linked-list/
# def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#     prev, curr = None, head
#     while curr:
#         next = curr.next
#         curr.next, prev = prev, curr
#         curr = next
#     return prev

# https://leetcode.com/problems/remove-linked-list-elements/submissions/
# def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#     prev, curr = None, head
#     while curr:
#         if curr.val == val:
#             if prev:
#                 prev.next = curr.next
#             else:
#                 head = curr.next
#             curr = curr.next
#         else:
#             prev, curr = curr, curr.next
#     return head


# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# def twoSum(self, numbers: List[int], target: int) -> List[int]:
#     seen = {}
#     for idx, num in enumerate(numbers):
#         target_num = target - num
#         if target_num in seen:
#             return [seen[target_num], idx+1]
#         seen[num] = idx + 1


# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# def minDepth(self, root: Optional[TreeNode]) -> int:
#     if root == None:
#         return 0
#     elif not root.left:
#         return self.minDepth(root.right) + 1
#     elif not root.right:
#         return self.minDepth(root.left) + 1
#     else:
#         return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#     if len(nums) == 0:
#         return None
    
#     mid = len(nums) // 2
#     left = self.sortedArrayToBST(nums[:mid])
#     right = self.sortedArrayToBST(nums[mid+1:])
#     node = TreeNode(nums[mid], left, right)
#     return node


# https://leetcode.com/problems/symmetric-tree/
# def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#     def isSymmetricBst(node1, node2):
#         if node1 == None and node2 == None:
#             return True
#         elif node1 == None or node2 == None:
#             return False
#         else:
#             return node1.val == node2.val and isSymmetricBst(node1.left, node2.right) and isSymmetricBst(node1.right, node2.left)
#     if not root:
#         return True
    
#     return isSymmetricBst(root.left, root.right)


# https://leetcode.com/problems/maximum-subarray/
# def maxSubArray(self, nums: List[int]) -> int:
#     maxSub = nums[0]
#     curSum = 0

#     for num in nums:
#         if curSum < 0:
#             curSum = 0
#         curSum += num
#         maxSub = max(maxSub, curSum)
#     return maxSub  


# https://leetcode.com/problems/search-insert-position/
# def searchInsert(self, nums: List[int], target: int) -> int:
#     left, right = 0, len(nums) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if target < nums[mid]:
#             right = mid - 1
#         elif target > nums[mid]:
#             left = mid + 1
#         else:
#             return mid
#     return mid if target < nums[mid] else mid + 1

# https://leetcode.com/problems/sqrtx/
# def mySqrt(self, x: int) -> int:
#     left, right = 0, x
#     ans = 0
#     while left <= right:
#         mid = (left + right) // 2

#         if mid*mid <= x:
#             ans = mid
#             left = mid+ 1
#         else:
#             right = mid -1
#     return ans


# https://leetcode.com/problems/search-in-rotated-sorted-array/

# https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/1700805/Short-Python-36ms-O(logn)-binary-search-with-explanation
# Intuition:

# The pivot index will be either in [left,middle] or [middle,right], which means one of the interval consist of ascending numbers. We can do a simple binary search there.

# Let's assume that there is no pivot between left and middle indices. If the target is in between nums[left] and nums[middle], then the target index has to be at [left,middle]. Otherwise, the target index has to be at [middle,right].

# We can do similar analysis if there is no pivot between middle and right indices.

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         #binary search
#         l,r = 0, len(nums)-1
        
#         while l<=r:
#             m = (l+r)//2
#             # if we find the target
#             if nums[m] == target:
#                 return m
#             if nums[l] == target:
#                 return l
#             if nums[r] == target:
#                 return r
            
#             if nums[l]<=nums[m]: #no pivot at [l,m]
#                 if nums[l]<=target<=nums[m]:
#                     r=m-1
#                 else:
#                     l=m+1
#             else: #no pivot at [m,r]
#                 if nums[m]<=target<=nums[r]:
#                     l=m+1
#                 else:
#                     r=m-1
                
#         return -1

# https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/1667748/Python-oror-Modified-Binary-Search-oror-O(log-N)
# def search(self, nums: List[int], target: int) -> int:
#         hi = len(nums)-1
#         lo = 0
        
#         while lo <= hi:
#             mid = (lo + hi)//2  
#             if nums[mid] == target:
#                 return mid
            
#             if nums[lo] <= nums[mid]: 
#                 if target in range(nums[lo], nums[mid]+1):
#                     hi = mid - 1     
#                 else:
#                     lo = mid + 1
          
#             else:                     
#                 if target in range(nums[mid], nums[hi]+1):
#                     lo = mid + 1
#                 else:
#                     hi = mid - 1
#         return -1
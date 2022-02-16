# https://leetcode.com/problems/first-bad-version/
# Example 1:

# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
# Example 2:

# Input: n = 1, bad = 1
# Output: 1

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

### O(log(n))
class Solution:
    def firstBadVersion(self, n):
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid -1 # is there anything less than mid
            else:
                left = mid + 1
        return left
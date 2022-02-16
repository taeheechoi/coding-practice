# https://leetcode.com/problems/insert-interval/
# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         intervals.append(newInterval)
#         intervals.sort(key=lambda x:x[0])
#         r = [intervals[0]]
#         for interval in intervals[1:]:
#             if r[-1][1] >= interval[0]:
#                 r[-1][1] = max(r[-1][1], interval[1])
#             else:
#                 r.append(interval)
#         return r
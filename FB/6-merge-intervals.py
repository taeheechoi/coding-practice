# https://leetcode.com/problems/merge-intervals/

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals = sorted(intervals)
#         tmp = intervals[0]
#         ans = []
#         for i in range(1,len(intervals)):
#             if tmp[0] <= intervals[i][0] <= tmp[1]:
#                 tmp = [tmp[0],max(intervals[i][1],tmp[1])]
#             else:
#                 ans.append(tmp)
#                 tmp = intervals[i]
#         ans.append(tmp)
#         return ans


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        r = [intervals[0]]
        
        for interval in intervals[1:]:
            if r[-1][1] >= interval[0]:
                r[-1][1] = max(r[-1][1], interval[1])
            else:
                r.append(interval)
        return r        
        
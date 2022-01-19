# https://leetcode.com/problems/relative-ranks/
# Example 1:

# Input: score = [5,4,3,2,1]
# Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
# Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
# Example 2:

# Input: score = [10,3,8,9,4]
# Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
# Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        prize = {}
        sorted_score = sorted(score, reverse=True)
        result = []
        for i in range(len(score)):
            if i == 0:
                prize[sorted_score[i]] = 'Gold Medal'
            elif i == 1:
                prize[sorted_score[i]] = 'Silver Medal'
            elif i == 2:
                prize[sorted_score[i]] = 'Bronze Medal'
            else:
                prize[sorted_score[i]] = str(i+1)
        
       
        for s in score:
            result.append(prize[s])
        print(result)

# https://leetcode.com/problems/keyboard-row/
# Example 1:

# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]
# Example 2:

# Input: words = ["omk"]
# Output: []
# Example 3:

# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')
        result = []
        for word in words:
            w = set(word.lower())
            if len(w | set1) == len(set1) or len(w | set2) == len(set2) or len(w | set3) == len(set3):
                result.append(word)
        return result
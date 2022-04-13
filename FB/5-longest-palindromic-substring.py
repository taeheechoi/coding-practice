class Solution:
    # Time O(N^2) Space O(1)
    def longestPalindrome(self, s):
        res = ''
        for i in range(len(s)):
            odd = self.is_pal(s, i, i)
            even = self.is_pal(s, i, i+1)
            res = max(odd, even, res, key=len)

        return res

    def is_pal(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1: r]
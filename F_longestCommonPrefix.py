# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longestCommonPrefix(words):
    charCount = {}

    for word in words:
        for char in word:
            if char in charCount:
                charCount[char] += 1
            else:
                charCount[char] = 1
    
    return ''.join([k for k, v in charCount.items() if v == len(words)])
        

print(longestCommonPrefix(["dog","racecar","car"]))
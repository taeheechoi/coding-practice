# https://leetcode.com/problems/reverse-only-letters/submissions/
# Example 1:

# Input: s = "ab-cd"
# Output: "dc-ba"
# Example 2:

# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:

# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"

def reverseOnlyLetters(s):
    left, right = 0, len(s) - 1
    l = list(s)
    
    while left < right:
        if not l[left].isalpha():
            left +=1
            continue
        if not l[right].isalpha():
            right -=1
            continue
        
        l[left], l[right] = l[right], l[left]
        left, right = left+1, right -1
    return ''.join(l)

reverseOnlyLetters('ab-cd')

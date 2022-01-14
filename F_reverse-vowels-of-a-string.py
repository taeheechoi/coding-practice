# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"

def reverseVowels(self, s: str) -> str:
    v = ['a','e','i','o','u','A','E','I','O','U']
    p1 = 0
    p2 = len(s) - 1
    
    result = list(s)
    
    while p1 <= p2:
        if result[p1] not in v:
            p1 +=1
        elif result[p2] not in v:
            p2 -= 1
        else:
            result[p1], result[p2] = result[p2], result[p1]
            
            p1 += 1
            p2 -= 1
    return ''.join(result)
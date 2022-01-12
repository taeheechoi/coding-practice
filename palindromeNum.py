# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# def isPalindrome(n):
#     str_num = str(n)

#     return True if str_num == str_num[::-1] else False

def isPalindrome(n):
    if n < 0: return False

    tmp = 0
    while tmp < n:
        tmp = tmp * 10 + n % 10
        n = n // 10
    


print(isPalindrome(424))
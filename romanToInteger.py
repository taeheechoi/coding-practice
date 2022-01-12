# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.

roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000 
}

# def romanToInteger(chars):
#     num = []
#     for char in chars:
#         num.append(roman[char])
#     return sum(num)

def romanToInteger(chars):
    result = 0

    for idx in range(len(chars) - 1):
        if roman[chars[idx]] < roman[chars[idx + 1]]:
            result -= roman[chars[idx]]
        else:
            result += roman[chars[idx]]
    
    result += roman[chars[-1]]
    return result

print(romanToInteger('MCMXCIV'))

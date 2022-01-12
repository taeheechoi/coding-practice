# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

def addBinary(a, b):
    return str(bin(int(a, 2) + int(b, 2)))[2:]

print(addBinary("11", "1"))
def isPalindrom(s):
    word = ''.join(filter(str.isalnum, s)).lower()
    return word == word[::-1]
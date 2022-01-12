def fibonacci(n):
    if n < 0: print('Incorrect number')
    elif n == 0: return 0
    elif n == 1: return 1
    else:
        a = 0
        b = 1
        for _ in range(1, n):
            a, b = b, a+b
        return b

print(fibonacci(9))
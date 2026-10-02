def func2(n):
    if n <= 2:
        return 2
    return func2(n-2) + 1

print(func2(16))
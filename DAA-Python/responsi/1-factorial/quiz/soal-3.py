from math import factorial


def func3(n):
    if n == 1:
        return 2 * (factorial(n+1))
    return func3(n-1) + (n+1)

print(func3(7))
def mystery(n):
    if n <= 0:
        return 0
    return n + mystery(n-2)

print(mystery(7))
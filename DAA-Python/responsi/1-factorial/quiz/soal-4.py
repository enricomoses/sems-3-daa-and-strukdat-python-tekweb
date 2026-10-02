def mystery(n):
    if n == 1:
        print('A')
        return
    print('B')
    mystery(n-1)
    print('C')

print(mystery(3))
def hitung_pangkat(x, y):
    if y == 1:
        return x, str(x)
    else:
        hasil, langkah = hitung_pangkat(x, y - 1)
        return x * hasil, f"{x} x {langkah}"

def print_pangkat(x, y):
    if y == 0:
        print(f"{x}^0 = 1")
    else:
        hasil, langkah = hitung_pangkat(x, y)
        print(f"{x}^{y} = {langkah} = {hasil}")

# x, y = 2, 3
x = int(input('Masukkan x: '))
y = int(input('Masukkan y: '))
print_pangkat(x, y)

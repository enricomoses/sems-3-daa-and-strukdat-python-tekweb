def fpb(a, b):
    if b == 0:
        return a
    else:
        return fpb(b, a % b)

# a, b = 48, 18
a = int(input('Masukkan a: '))
b = int(input('Masukkan b: '))
hasil_fpb = fpb(a, b)
print(f"FPB dari {a} dan {b} adalah {hasil_fpb}")
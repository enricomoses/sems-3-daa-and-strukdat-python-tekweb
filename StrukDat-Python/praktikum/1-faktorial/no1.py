def hitung_pangkat(x, y):
    if y == 1:
        return x, str(x)
    else:
        hasil, langkah = hitung_pangkat(x, y - 1)
        return x * hasil, f"{x} x {langkah}"

def tampilkan_pangkat(x, y):
    if y == 0:
        print(f"{x}^0 = 1")
    else:
        hasil, langkah = hitung_pangkat(x, y)
        print(f"{x}^{y} = {langkah} = {hasil}")


def fpb(a, b):
    if b == 0:
        return a
    else:
        return fpb(b, a % b)

def hitung_faktorial(n):
    if n == 1 or n == 0:
        return 1, "1"
    else:
        hasil, langkah = hitung_faktorial(n - 1)
        return n * hasil, f"{n} x {langkah}"


def tampilkan_faktorial_dan_bagi(n, k):
    hasil_fak, langkah_fak = hitung_faktorial(n)
    print(f"Faktorial dari {n} adalah {langkah_fak} = {hasil_fak}")

    hasil_bagi = hasil_fak / k
    print(f"Hasil bagi faktorial {n} dengan {k} adalah {hasil_fak} / {k} = {hasil_bagi:g}")


x, y = 2, 3
tampilkan_pangkat(x, y)

a, b = 48, 18
hasil_fpb = fpb(a, b)
print(f"FPB dari {a} dan {b} adalah {hasil_fpb}")

n, k = 5, 2
tampilkan_faktorial_dan_bagi(n, k)
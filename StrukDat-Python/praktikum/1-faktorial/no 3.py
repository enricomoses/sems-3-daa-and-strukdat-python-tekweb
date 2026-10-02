def hitung_faktorial(n):
    if n == 1 or n == 0:
        return 1, "1"
    else:
        hasil, langkah = hitung_faktorial(n - 1)
        return n * hasil, f"{n} x {langkah}"

def print_faktorial_dan_bagi(n, k):
    hasil_fak, langkah_fak = hitung_faktorial(n)
    print(f"Faktorial dari {n} adalah {langkah_fak} = {hasil_fak}")

    hasil_bagi = hasil_fak / k
    print(f"Hasil bagi faktorial {n} dengan {k} adalah {hasil_fak} / {k} = {hasil_bagi:g}")

# n, k = 5, 2
n = int(input('Masukkan n: '))
k = int(input('Masukkan k: '))
print_faktorial_dan_bagi(n, k)
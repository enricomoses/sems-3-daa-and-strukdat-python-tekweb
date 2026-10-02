def hanoi(n, asal, bantu, tujuan, offset=0, tampilkan=True):
    # base case
    # Tidak ada cakram yang perlu dipindahkan, jadi 0 langkah dikerjakan.
    if n == 0:
        return 0

    # recursive case
    # Langkah 1: pindahkan (n-1) cakram teratas dari ASAL ke BANTU.
    # Perhatikan peran tiang bertukar: tujuan kini berfungsi sebagai tiang bantuan.
    langkah_kiri = hanoi(n - 1, asal, tujuan, bantu, offset, tampilkan)

    # Langkah 2: sekarang cakram terbesar (cakram ke-n) sendirian di asal,
    # sehingga bisa langsung dipindahkan ke tujuan.
    nomor = offset + langkah_kiri + 1 # nomor urut langkah ini
    if tampilkan: # cetak detail perpindahan
        print(f"Langkah {nomor:>3}: cakram {n} dipindahkan dari tiang {asal} ke tiang {tujuan}")

    # Langkah 3: pindahkan kembali (n-1) cakram dari BANTU ke TUJUAN,
    # kali ini ASAL yang berperan sebagai tiang bantuan.
    langkah_kanan = hanoi(n - 1, bantu, asal, tujuan, nomor, tampilkan)


    # Total langkah = langkah subproblem kiri + 1 langkah cakram terbesar + subproblem kanan
    return langkah_kiri + 1 + langkah_kanan



N = 3 # jumlah cakram yang diuji
total = hanoi(N, "A", "B", "C") # jalankan algoritma rekursif
print(f"\nTotal pemindahan yang terjadi : {total}") # poin tambahan (1)
print(f"Rumus langkah minimum 2^N - 1  : {2 ** N - 1}") # pembuktian bahwa hasil minimum

# Uji beberapa nilai N untuk membuktikan pola 2^N - 1 (tanpa mencetak langkahnya)
print()
print(f"{'N':>3}{'Total Langkah':>16}{'2^N - 1':>10}")
for n in range(1, 11):                               # coba N = 1 sampai 10
    jumlah = hanoi(n, "A", "B", "C", tampilkan=False)  # hitung saja, tidak dicetak
    print(f"{n:>3}{jumlah:>16}{2 ** n - 1:>10}")
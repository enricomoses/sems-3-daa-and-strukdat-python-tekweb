def tukar_kupon(jumlah, syarat, dapat, level=0, verbose=False):
    # validasi awal
    if syarat <= 0 or dapat < 0: # parameter tidak masuk akal
        raise ValueError("syarat harus > 0 dan dapat harus >= 0")
    if dapat >= syarat: # kupon tidak pernah berkurang
        raise ValueError("dapat harus < syarat, jika tidak proses tidak akan pernah berhenti")

    # base case
    # Kupon yang dipegang sudah lebih sedikit daripada syarat penukaran,
    # sehingga tidak ada lagi penukaran yang bisa dilakukan. Proses berhenti.
    if jumlah < syarat:
        if verbose: # cetak kondisi akhir bila diminta
            print(f"{'  ' * level}[BASE CASE] sisa {jumlah} kupon < syarat {syarat} -> berhenti")
        return (0, 0, jumlah) # 0 kupon baru, 0 penukaran, sisa = jumlah

    # recursive casae
    penukaran = jumlah // syarat # berapa kali tukar dilakukan ronde ini
    kupon_baru = penukaran * dapat # kupon baru yang diterima ronde ini
    tidak_terpakai = jumlah % syarat # kupon yang belum cukup untuk ditukar
    dipegang = tidak_terpakai + kupon_baru # modal untuk ronde/subproblem berikutnya

    if verbose: # menampilkan jejak tiap ronde
        print(f"{'  ' * level}[RONDE {level + 1}] punya {jumlah} -> tukar {penukaran}x "
              f"-> dapat {kupon_baru} baru, sisa belum tertukar {tidak_terpakai} "
              f"-> bawa {dipegang} ke rekursi berikutnya")

    # Subproblem: masalah yang sama persis tetapi dengan jumlah kupon lebih kecil
    baru_lanjutan, tukar_lanjutan, sisa_akhir = tukar_kupon(
        dipegang, syarat, dapat, level + 1, verbose
    )

    # Solusi masalah besar = hasil ronde ini + solusi subproblem yang lebih kecil
    return (kupon_baru + baru_lanjutan, # total seluruh kupon baru
            penukaran + tukar_lanjutan, # total seluruh penukaran
            sisa_akhir) # sisa kupon dari base case terdalam


def laporan(nama, awal, syarat, dapat, verbose=False):
    # Mencetak laporan lengkap untuk satu jenis kupon
    print(f"\n=== KUPON {nama.upper()} (awal {awal}, tukar {syarat} dapat {dapat}) ===")
    baru, penukaran, sisa = tukar_kupon(awal, syarat, dapat, verbose=verbose) # panggil rekursi
    total_pernah = awal + baru # kupon awal + seluruh kupon baru
    print(f"Total kupon yang pernah didapat : {total_pernah}") # jawaban utama
    print(f"Jumlah kupon baru dari penukaran: {baru}") # hasil murni penukaran
    print(f"Jumlah penukaran yang terjadi   : {penukaran}") # poin tambahan (a)
    print(f"Sisa kupon tidak dapat ditukar  : {sisa}") # poin tambahan (b)
    return total_pernah, penukaran, sisa # dikembalikan bila ingin dipakai lagi


# ---------------- PROGRAM UTAMA ----------------
# Data kasus pada soal: (nama jenis, jumlah awal, syarat tukar, jumlah kupon baru)
data = [
    ("Emas",    40, 4, 2), # 4 emas -> 2 emas
    ("Perak",   30, 3, 1), # 3 perak -> 1 perak
    ("Perunggu", 20, 2, 1), # 2 perunggu -> 1 perunggu
]

hasil = [] # menampung ringkasan tiap jenis
for nama, awal, syarat, dapat in data: # proses setiap jenis kupon
    hasil.append((nama,) + laporan(nama, awal, syarat, dapat, verbose=True))

print()
print(f"{'Jenis':<10}{'Total Didapat':>15}{'Penukaran':>12}{'Sisa':>8}")
for nama, total, penukaran, sisa in hasil: # cetak baris per jenis kupon
    print(f"{nama:<10}{total:>15}{penukaran:>12}{sisa:>8}")
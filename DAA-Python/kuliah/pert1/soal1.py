def cek_elemen_hashset(S, x):
    seen = set()  # O(n) space

    for angka in S:  # O(n) time
        target = x - angka
        if target in seen:
            return True  # ada
        seen.add(angka)

    return False  # tidak ada


# Contoh penggunaan
S = [1, 2, 3, 5, 10]
x1 = 7
x2 = 9

print(f"x = {x1} -> {'ada' if cek_elemen_hashset(S, x1) else 'tidak ada'}")
print(f"x = {x2} -> {'ada' if cek_elemen_hashset(S, x2) else 'tidak ada'}")
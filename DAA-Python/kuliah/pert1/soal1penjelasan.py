S = [1, 2, 3, 5, 10]
x = 7 # 2 + 5
ada = False
seen = set()
for angka in S:
    target = x - angka
    if target in seen:
        ada = True
        break
    seen.add(angka)

print(ada)
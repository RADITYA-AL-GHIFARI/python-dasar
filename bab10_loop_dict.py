nilai = {"mtk": 80, "ipa": 75, "bhs": 90}
for mapel, angka in nilai.items():
    print(mapel, "=", angka)
print(list(nilai.keys()))
print(list(nilai.values()))
print("mtk" in nilai)
print(sum(nilai.values()) / len(nilai))

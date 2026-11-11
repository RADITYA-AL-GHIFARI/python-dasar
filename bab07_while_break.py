hitung = 1
while hitung <= 5:
    if hitung == 2:
        hitung += 1
        continue
    if hitung == 4:
        break
    print("Hitung", hitung)
    hitung += 1
print("Selesai")

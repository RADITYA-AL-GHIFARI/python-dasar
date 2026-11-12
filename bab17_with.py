with open("data.txt", "r") as file:
    isi = file.read()
    print(isi)

# Contoh program lengkap
with open("contoh.txt", "w") as file:
    file.write("Belajar Python itu menyenangkan!\n")

with open("contoh.txt", "a") as file:
    file.write("Tambahan baris kedua.\n")

with open("contoh.txt", "r") as file:
    for baris in file:
        print(baris.strip())

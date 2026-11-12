# Menulis file baru atau menimpa file lama
file = open("data.txt", "w")
file.write("Halo, ini data baru!\n")
file.write("Baris kedua...\n")
file.close()

# Menambah data di akhir file
file = open("data.txt", "a")
file.write("Baris tambahan...\n")
file.close()

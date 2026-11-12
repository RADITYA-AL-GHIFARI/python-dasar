file = open("data.txt", "r")  # "r" = read
print(file.read())
file.close()

file = open("data.txt", "r")
for baris in file:
    print(baris.strip())  # strip() untuk hapus newline
file.close()

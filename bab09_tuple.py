titik = (3, 4)
print(titik[0], titik[1])
x, y = titik
print("x =", x, "y =", y)
print(len(titik), titik.count(3))
try:
    titik[0] = 9
except TypeError:
    print("Tuple tidak bisa diubah")

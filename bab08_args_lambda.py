def jumlah(*angka):
    return sum(angka)

print(jumlah(1, 2, 3, 4))
kuadrat = lambda x: x ** 2
print(kuadrat(6))

def info(**data):
    for k, v in data.items():
        print(k, "=", v)

info(nama="Raditya", sekolah="SMKN 2 Subang")

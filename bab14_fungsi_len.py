class Kucing:
    def suara(self):
        return "Meow"

class Anjing:
    def suara(self):
        return "Guk guk"

def cetak_suara(hewan):
    print(hewan.suara())

cetak_suara(Kucing())
cetak_suara(Anjing())

print(len("Python"))  # string
print(len([1, 2, 3]))  # list
print(len({"a": 1, "b": 2}))  # dictionary

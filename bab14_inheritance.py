class Hewan:
    def suara(self):
        return "Hewan bersuara"

class Kucing(Hewan):
    def suara(self):
        return "Meow"

class Anjing(Hewan):
    def suara(self):
        return "Guk guk"

# Semua objek diperlakukan sama sebagai Hewan
daftar_hewan = [Kucing(), Anjing(), Hewan()]
for h in daftar_hewan:
    print(h.suara())

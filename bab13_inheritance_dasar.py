# Parent class
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        print("Hewan ini memiliki suara.")

# Child class
class Kucing(Hewan):
    def suara(self):
        print(f"{self.nama} mengeong: Meow!")

class Anjing(Hewan):
    def suara(self):
        print(f"{self.nama} menggonggong: Guk guk!")

# Membuat objek dari class turunan
kucing = Kucing("Tom")
anjing = Anjing("Spike")

kucing.suara()
anjing.suara()

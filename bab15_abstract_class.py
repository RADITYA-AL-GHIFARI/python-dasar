from abc import ABC, abstractmethod

# Abstract class
class Hewan(ABC):
    @abstractmethod
    def suara(self):
        pass

# Subclass yang mengimplementasikan abstract method
class Kucing(Hewan):
    def suara(self):
        return "Meow"

class Anjing(Hewan):
    def suara(self):
        return "Guk guk"

# Tidak bisa langsung membuat object dari class abstract
# h = Hewan()  # Error!

# Hanya bisa dari subclass
k = Kucing()
a = Anjing()
print(k.suara())
print(a.suara())

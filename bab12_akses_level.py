class Contoh:
    def __init__(self):
        self.nama = "Raditya"        # public
        self._alamat = "contoh alamat"  # protected
        self.__saldo = 1000          # private

obj = Contoh()
print(obj.nama)
print(obj._alamat)
try:
    print(obj.__saldo)
except AttributeError:
    print("Atribut private tidak bisa diakses langsung")

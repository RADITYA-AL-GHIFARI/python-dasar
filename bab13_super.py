class Mahasiswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    def info(self):
        print(f"Nama: {self.nama}, Jurusan: {self.jurusan}")

class MahasiswaBaru(Mahasiswa):
    def __init__(self, nama, jurusan, tahun_masuk):
        super().__init__(nama, jurusan)  # memanggil constructor parent
        self.tahun_masuk = tahun_masuk

    def info(self):
        super().info()  # memanggil method parent
        print(f"Tahun Masuk: {self.tahun_masuk}")

maba = MahasiswaBaru("Andi", "Informatika", 2025)
maba.info()

siswa = {"nama": "Raditya", "kelas": "XI RPL"}
print(siswa["nama"])
print(siswa.get("sekolah", "tidak ada"))
siswa["sekolah"] = "SMKN 2 Subang"
siswa["kelas"] = "XI RPL 1"
print(siswa)
del siswa["kelas"]
print(len(siswa))

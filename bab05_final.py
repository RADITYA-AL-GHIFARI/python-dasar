from typing import Final
BATAS_NILAI: Final = 75
print("Batas lulus:", BATAS_NILAI)
nilai = 80
print("Lulus" if nilai >= BATAS_NILAI else "Belum lulus")

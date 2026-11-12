# Python Dasar

Praktikum **Belajar Python Dasar** (Santrikoding, 19 artikel) untuk mata pelajaran Pemrograman Web, SMKN 2 Subang.

- Nama: Raditya Al Ghifari
- Kelas: XI RPL
- Lingkungan: Arch Linux (WSL2), Python 3.14, virtual environment `venv`

## Cara Menjalankan

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python bab01_hello.py
```

Bab 18 dan 19 dijalankan dari folder utama proyek (agar `matematika.py` dan `my_package/` terbaca). Bab 17 dijalankan berurutan: `bab17_tulis_file.py`, `bab17_baca_file.py`, `bab17_with.py`.

## Daftar Bab dan Berkas

1. Pengenalan & Instalasi Python: `bab01_hello.py`, `bab01_versi.py`
2. Struktur Dasar Program Python: `bab02_struktur.py`, `bab02_format_output.py`
3. Tipe Data Dasar: `bab03_tipe_data.py`, `bab03_konversi.py`
4. Variable: `bab04_variable.py`, `bab04_aturan_nama.py`
5. Konstanta: `bab05_konstanta.py`, `bab05_final.py`
6. Operator: `bab06_aritmatika.py`, `bab06_perbandingan_logika.py`, `bab06_assignment.py`
7. Control Flow: `bab07_if_else.py`, `bab07_for_loop.py`, `bab07_while_break.py`
8. Function: `bab08_function_dasar.py`, `bab08_parameter.py`, `bab08_args_lambda.py`
9. List, Tuple, dan Set: `bab09_list.py`, `bab09_tuple.py`, `bab09_set.py`
10. Dictionary: `bab10_dictionary.py`, `bab10_loop_dict.py`
11. Class & Object (OOP Dasar): `bab11_class_object.py`, `bab11_atribut_method.py`, `bab11_encapsulation_dasar.py`
12. Encapsulation: `bab12_akses_level.py`, `bab12_encapsulation.py`
13. Inheritance: `bab13_inheritance_dasar.py`, `bab13_method_baru.py`, `bab13_super.py`
14. Polymorphism: `bab14_polymorphism_dasar.py`, `bab14_inheritance.py`, `bab14_fungsi_len.py`
15. Abstraction: `bab15_abstract_class.py`, `bab15_pembayaran.py`
16. Exception Handling: `bab16_try_except.py`, `bab16_banyak_error.py`, `bab16_else_finally.py`, `bab16_raise.py`
17. File Handling (Read & Write File): `bab17_tulis_file.py`, `bab17_baca_file.py`, `bab17_with.py`
18. Module: `matematika.py`, `bab18_main.py`, `bab18_alias.py`, `bab18_from_import.py`, `bab18_builtin.py`
19. Package: `my_package/`, `bab19_package.py`, `bab19_import_fungsi.py`, `bab19_stdlib.py`

## Catatan

- Bukti hasil eksekusi ada di folder `screenshots/`.
- Riwayat commit dibuat per bab dengan format `feat(dasar): ... seri artikel #N`.
- Contoh kode bab 11 sampai 19 mengikuti contoh pada artikel Santrikoding; bab 1 sampai 10 disusun sesuai topik bab yang sama.

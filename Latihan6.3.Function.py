# Program: Implementasi Keyword Argument

# Membuat function dengan beberapa parameter untuk pengaturan tema website
def atur_tema_website(warna_latar, warna_teks, font_utama):
    print("=== Konfigurasi Tema Website ===")
    print("Warna Latar :", warna_latar)
    print("Warna Teks  :", warna_teks)
    print("Font Utama  :", font_utama)
    print("-" * 30)

# Memanggil function (urutan harus sesuai)
atur_tema_website("Soft Pink", "Soft Blue", "Arial")

# Memanggil function (urutan bisa acak)
atur_tema_website(font_utama="Gothic", warna_latar="Hitam", warna_teks="Merah")
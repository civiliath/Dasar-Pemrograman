# Program: Implementasi Semua Komponen Materi String dan Manipulasi String

# PEMBUATAN STRING (KUTIP TUNGGAL DAN KUTIP GANDA)
# String dapat dibuat menggunakan kutip tunggal (') atau kutip ganda (")
nama_depan = 'Budi'          # Contoh menggunakan kutip tunggal
nama_belakang = "Saputra"    # Contoh menggunakan kutip ganda

# MENGGABUNGKAN STRING (+) DAN KONVERSI TIPE DATA str()
# Menggabungkan string dengan tipe data lain wajib dikonversi ke string dahulu menggunakan str()
umur = 25
info_pesan = "Nama saya " + nama_depan + " " + nama_belakang + " dan Umur " + str(umur) + " tahun."

print("=== 1 & 2. Pembuatan, Penggabungan String & str() ===")
print(info_pesan)
print("-" * 60)

# MENGETAHUI PANJANG STRING DENGAN len()
# Function len() digunakan untuk menghitung total jumlah karakter termasuk spasi
panjang_karakter = len(info_pesan)

print("=== 3. Panjang String dengan len() ===")
print(f"Panjang total karakter teks di atas adalah: {panjang_karakter} karakter.")
print("-" * 60)

# ESCAPE CHARACTERS (\n, \t, \\, \", \')
# Aturan khusus untuk memasukkan karakter yang biasanya memiliki arti sintaksis
# \n (Baris Baru), \t (Tab), \\ (Backslash), \" (Kutip Ganda), \' (Kutip Tunggal)
teks_escape = "=== 4. Escape Characters ===\n\tDetail Data:\n\t- Status:\t\"Aktif\"\n\t- Direktori:\tC:\\Aplikasi\\Data\n\t- Catatan:\tHari Jum\'at libur"

print(teks_escape)
print("-" * 60)

# METODE STRING (count DAN find)
teks_materi = "Python adalah bahasa pemrograman yang populer. Belajar Python sangat menyenangkan!"

# count(text) digunakan untuk menghitung berapa kali kata/teks tersebut muncul
jumlah_kata_python = teks_materi.count("Python")

# find(text) digunakan untuk mencari posisi indeks pertama kali teks tersebut ditemukan
posisi_kata_populer = teks_materi.find("populer")

print("=== 5. Metode String (count & find) ===")
print("Teks Acuan:", teks_materi)
print("Jumlah kata 'Python' muncul     :", jumlah_kata_python, "kali")
print("Kata 'populer' ada pada indeks  :", posisi_kata_populer)
print("-" * 60)

# STRING INTERPOLATION (f-strings)
# Cara modern dan efisien menggabungkan variabel dengan menambah huruf 'f' di awal string
# Variabel langsung dipanggil di dalam kurung kurawal {}
ipk = 3.85
pesan_fstring = f"Mahasiswa bernama {nama_depan} {nama_belakang} memiliki nilai IPK {ipk}."

print("=== 6. String Interpolation (f-strings) ===")
print(pesan_fstring)
print("-" * 60)

# f-strings DENGAN EXPRESSIONS
# f-strings juga dapat mengeksekusi ekspresi matematika atau logika langsung di dalamnya
print("=== 7. f-strings dengan Expressions ===")
# Ekspresi Matematika (Pengurangan tahun saat ini dengan umur)
print(f"Jika saat ini tahun 2026, maka {nama_depan} lahir pada tahun {2026 - umur}.")

# Ekspresi Logika / Kondisional (Ternary Operator)
print(f"Status kedewasaan: {'Sudah Dewasa' if umur >= 17 else 'Belum Dewasa'}")

# Ekspresi Pemanggilan Fungsi pada variabel di dalam f-string
print(f"Nama Lengkap (Kapital): {nama_depan.upper()} {nama_belakang.upper()}")
print("============================================================")
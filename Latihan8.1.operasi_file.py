# Program: Implementasi Operasi File I/O dengan Seluruh Mode (x, w, r, a)

# Nama file teks yang akan digunakan dalam operasi
nama_file = "data_akademik.txt"

# =========================================================================
# 1. IMPLEMENTASI MODE 'x' (Create)
# Membuat file baru. Akan menghasilkan error jika file sudah ada.
# =========================================================================
print("=== 1. Mencoba Mode 'x' (Create) ===")
try:
    # Membuka file dengan mode 'x' menggunakan 'with statement' agar otomatis tertutup
    with open(nama_file, "x") as file:
        # Menulis baris awal ke dalam file baru
        file.write("=== DATA UTAMA AKADEMIK ===\n")
    print(f"[Sukses]: File '{nama_file}' berhasil dibuat baru.")
except FileExistsError:
    # Menangani error jika file ternyata sudah pernah dibuat sebelumnya
    print(f"[Pesan]: File '{nama_file}' sudah ada, tidak bisa dibuat baru dengan mode 'x'.")

print("-" * 50)


# =========================================================================
# 2. IMPLEMENTASI MODE 'w' (Write)
# Menulis data ke file. Akan membuat file baru atau menimpa data lama.
# =========================================================================
print("=== 2. Mencoba Mode 'w' (Write) ===")
try:
    with open(nama_file, "w") as file:
        # Menulis atau menimpa isi file dengan data mahasiswa baru
        file.write("1. Budi Saputra, IPK: 3.85\n")
        file.write("2. Siti Aminah,  IPK: 3.92\n")
    print("[Sukses]: Data berhasil ditulis (menimpa isi file sebelumnya jika ada).")
except Exception as e:
    print(f"[Error]: Gagal menulis ke file. Alasan: {e}")

print("-" * 50)


# =========================================================================
# 3. IMPLEMENTASI MODE 'r' (Read)
# Membaca isi file yang sudah ada. Error jika file tidak ditemukan.
# =========================================================================
print("=== 3. Mencoba Mode 'r' (Read) ===")
try:
    with open(nama_file, "r") as file:
        print("Isi file saat ini:")
        # Membaca isi file baris demi baris menggunakan perulangan (loop)
        for line in file:
            # Menggunakan strip() untuk menghapus spasi/pindah baris ekstra di ujung teks
            print(line.strip())
except FileNotFoundError:
    # Menangani error jika file yang ingin dibaca tidak ada di direktori
    print(f"[Error]: File '{nama_file}' tidak ditemukan!")

print("-" * 50)


# =========================================================================
# 4. IMPLEMENTASI MODE 'a' (Append)
# Menambahkan data baru di akhir file tanpa menghapus data lama.
# =========================================================================
print("=== 4. Mencoba Mode 'a' (Append) ===")
try:
    with open(nama_file, "a") as file:
        # Menambahkan data mahasiswa baru di baris paling bawah
        file.write("3. Ahmad Fauzi,  IPK: 3.70\n")
    print("[Sukses]: Data baru berhasil ditambahkan di akhir file.")
except Exception as e:
    print(f"[Error]: Gagal menambahkan data. Alasan: {e}")

print("-" * 50)


# =========================================================================
# VERIFIKASI AKHIR: Membaca kembali hasil gabungan setelah mode 'a'
# =========================================================================
print("=== Tampilan Akhir Data File setelah di-Append ===")
try:
    with open(nama_file, "r") as file:
        # Menampilkan seluruh baris teks yang kini sudah bertambah
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print(f"[Error]: File '{nama_file}' tidak ditemukan!")
print("=== Selesai ===")
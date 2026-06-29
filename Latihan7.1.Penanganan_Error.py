# Program: Implementasi try-except untuk menangani berbagai jenis error spesifik

try:
    print("--- Simulasi Deteksi Error ---")
    # Memicu IndexError (Mengakses indeks di luar jangkauan list)
    list_data = [10, 20, 30]
    print("Mengakses data indeks ke-5:", list_data[5])

except ValueError:
    # Dieksekusi jika terjadi kesalahan nilai atau kegagalan konversi tipe data 
    print("[Error Terdeteksi]: Nilai tidak valid atau gagal dikonversi!")

except ZeroDivisionError:
    # Dieksekusi jika terdapat operasi pembagian dengan angka nol 
    print("[Error Terdeteksi]: Tidak bisa melakukan pembagian dengan angka nol!")

except IndexError:
    # Dieksekusi jika mengakses posisi indeks list yang tidak ditemukan 
    print("[Error Terdeteksi]: Indeks tidak ditemukan atau di luar jangkauan list!")

except:
    # Menangkap segala jenis kesalahan lain yang belum didefinisikan di atas 
    print("[Error Terdeteksi]: Terjadi kesalahan jenis lainnya!")
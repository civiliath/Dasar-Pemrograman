# Program: Implementasi Function dengan Parameter dan Return Value

# Membuat function dengan tiga parameter untuk menerima input nilai
def hitung_nilai_akhir(tugas, uts, uas):
    # Melakukan operasi matematika untuk mendapatkan rata-rata
    nilai_akhir = (tugas + uts + uas) / 3
    
    # Mengembalikan nilai hasil perhitungan
    return nilai_akhir

# Memanggil function
hasil_mahasiswa = hitung_nilai_akhir(80, 85, 90)

# Menampilkan hasil yang telah dikembalikan oleh function
print("Nilai akhir mahasiswa adalah:", hasil_mahasiswa)
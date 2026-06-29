# Menghitung Pengurangan Berantai Menggunakan Metode Rekursif
# jika diinput 5, proses pengurangan akan berjalan mundur hingga 1

# Mendefinisikan fungsi dengan pendekatan rekursi
def pengurangan(n):
    # Batas akhir eksekusi untuk menghentikan perulangan fungsi
    if n == 1:
        return 1
    # Mengurangi nilai saat ini dengan hasil pemanggilan fungsi berikutnya
    else:
        return n - pengurangan(n - 1)

# Mengambil input data angka dari pengguna
angka = int(input("Masukkan sebuah angka: "))

# Menjalankan fungsi rekursif dan menyimpan hasilnya ke dalam variabel
hasil = pengurangan(angka)

print("Hasil pengurangan rekursif =", hasil)
# Program: Implementasi Lengkap try, except, else, dan finally

try:
    print("=== PROGRAM PENGECEKAN ANGKA ===")
    # Meminta input dari pengguna dan langsung mengubahnya menjadi bilangan bulat
    # Jika pengguna memasukkan huruf/simbol, maka akan terjadi ValueError 
    angka = int(input("Masukkan sebuah angka bulat: "))

except ValueError:
    # Blok ini hanya berjalan jika terjadi error (input bukan angka bulat) 
    print("[Pesan]: Input yang Anda masukkan tidak valid! Harap masukkan angka.")

else:
    # Blok ini hanya berjalan jika blok 'try' berhasil tanpa ada error sama sekali 
    print(f"[Sukses]: Anda berhasil memasukkan angka {angka} ke dalam sistem.")
    
    # Logika tambahan untuk memeriksa angka genap atau ganjil
    if angka % 2 == 0:
        print("Keterangan: Angka tersebut termasuk bilangan GENAP.")
    else:
        print("Keterangan: Angka tersebut termasuk bilangan GANJIL.")

finally:
    # Blok ini akan selalu dijalankan, baik ketika terjadi error maupun sukses 
    print("[Sistem]: Pemrosesan selesai. Terima kasih telah menggunakan program ini.")
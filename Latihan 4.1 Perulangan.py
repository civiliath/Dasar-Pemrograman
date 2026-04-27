# latihan 4.1 perulangan

# menentukan bulan lahir saya
bulan_lahir = 6

# menampilkan bulan lahir
print("Bulan lahir saya :", bulan_lahir)

# menampilkan angka 1 sampai 100
# range(mulai 1, berhenti sebelum 101)
for i in range(1, 101):
    # cek angka apakh kelipatan 6 
    # % untuk mencari sisa bagi
    # kalau sisa baginya 0, berarti angkanya kelipatan 6
    if i % bulan_lahir == 0:
        print("Bulan")
    else:
        # kalo bukan kelipatan, ditampilkn angka biasa
        print(i)
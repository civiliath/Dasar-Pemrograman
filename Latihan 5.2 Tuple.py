# 5.2. implementasi tuple dan operasinya

# data bersifat tetap, informasi dasar mobil (merk, tahun, warna)
mobil = ("Mazda 3", 2019, "Merah")
print("Data mobil:")
print(mobil)

print( )

# menggunakan function len()
print("Jumlah kategori data mobil:")
print(len(mobil))

print( )

# menampilkan semua elemen satu per satu
print("Detail mobil:")
for info in mobil:
    print("-", info)
    
print( )

# menggunakan range dan len untuk membuat urutan
print("Data mobil dengan nomor urut:")
for i in range(len(mobil)):
    print(str(i + 1) + ".", mobil[i])
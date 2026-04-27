# 5.1 membuat program dengan implementasi list dan operasi list didalamnya

# list dgn string
lagu = ["Closer", "Outro", "Paranoia", "Sayang"]
print(lagu)

print( )

# mengakses elemen
print("Top songs Crawla saat ini:")
print(lagu[0]) # closer
print(lagu[1]) # outro
print(lagu[2]) # paranoia
print(lagu[3]) # sayang

print( )

# mengubah elemen list
# paranoia turun dari top songs
lagu[2] = "Halla" # Diubah ke index 2 agar sesuai komentar "paranoia"
print("Top songs Crawla setelah update:")
print(lagu)

print( )

# menambah elemen di akhir list menggunakan append()
lagu.append("Diary")
print("Top songs Crawla setelah rilis lagu baru:")
print(lagu)

print( )

# menghapus elemen menggunakan remove()
# Pastikan data "Sayang" masih ada di list sebelum di-remove
if "Sayang" in lagu:
    lagu.remove("Sayang")
print("Top songs Crawla setelah lagu Sayang terkena skandal:")
print(lagu)

print( )

# menghapus elemen terakhir menggunakan pop()
lagu.pop()
print("Top songs Crawla setelah lagu terakhir ditakedown:")
print(lagu)

print( )

# menghitung panjang list dengan len()
print("Jumlah lagu di dalam daftar top songs sekarang:")
print(len(lagu))

print( )

# Menggabungkan dua list
collab = ["Inferno", "Behave"]
gabungan = lagu + collab
print("Daftar top songs Crawla ft. Homies:")
print(gabungan)

print ( )

# menggunakan for loop 
print("Cetak daftar top songs Crawla ft. Homies satu per satu:")
for p in gabungan:
    print("-", p)
    
# PERBAIKAN: Sebelumnya 'primt', diubah menjadi 'print'
print( )

# dengan index
print("Daftar top songs Crawla ft. Homies dengan nomor urut:")
for i in range(len(gabungan)):
    print(str(i + 1) + ".", gabungan[i])
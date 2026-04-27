# 5.3 implementasi dictionary dan operasi  dictionary

# dictionary dengan data novel
novel = {
    "judul": "Laut Bercerita",
    "penulis": "Leila S. Chudori",
    "penerbit": "KPG"
}
print(novel)

print( )

print("Judul Novel:", novel["judul"])
print("Penulis:", novel["penulis"])
print("Penerbit:", novel["penerbit"])

print( )

# mengubah nilai (update) data yang sudah ada 
novel["penerbit"] = "Kepustakaan Populer Gramedia"
print("Data setelah penerbit diperbarui:", novel)

print( )

# menambah data baru ke dalam dictionary 
novel["penjualan"] = 500000
print("Data setelah ditambah penjualan:", novel)

print( )

# menghapus key-value
del novel["penerbit"]
print("Data setelah penerbit dihapus:", novel)

print( )

# mengiterasi key-valu pairs
for key in novel: 
    print(key, ":", novel[key])
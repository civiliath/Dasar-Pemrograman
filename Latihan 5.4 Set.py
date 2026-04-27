# 5.4 implementasi set dan operasi set

adobe = {"Photoshop", "Illustrator", "InDesign"}

print( )

# menampilkan isi set
print("Adobe family:", adobe)

print( )

# menambah data baru ke set menggunakan method add(value) 
adobe.add("After Effects")
print("Setelah ditambah After Effects:", adobe)

print( )

# menghapus data dari set menggunakan method remove(value) 
adobe.remove("InDesign")
print("Setelah InDesign dihapus:", adobe)

print( )

# menghitung jumlah data dalam set menggunakan len() 
print("Jumlah Adobe family saat ini:", len(adobe))

print( )

# menampilkan elemn
for e in adobe:
    print(e)
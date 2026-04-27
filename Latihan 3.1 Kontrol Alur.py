# latihan 3.1 kontrol alur

# minta input tahun lahir dari user
tahun_lahir = int(input("Masukkan tahun lahir Anda: "))

# pengecekan masuk kategori generasi apa
if 1928 <= tahun_lahir <= 1945:
    generasi = "Silent Generation"
    keterangan = "Tumbuh selama Depresi Besar dan Perang Dunia II, dikenal pekerja keras, sabar, dan hemat."
elif 1946 <= tahun_lahir <= 1964:
    generasi = "Baby Boomers"
    keterangan = "Lahir setelah Perang Dunia II, generasi ini mengalami lonjakan kelahiran dan fokus pada pencapaian personal."
elif 1965 <= tahun_lahir <= 1980:
    generasi = "Generasi X"
    keterangan = "Dikenal mandiri, tumbuh di masa peralihan teknologi tradisional ke digital (komputer/internet)."
elif 1981 <= tahun_lahir <= 1996:
    generasi = "Generasi Y / Milenial"
    keterangan = "Generasi yang melek teknologi (digital natives) dan peduli isu sosial."
elif 1997 <= tahun_lahir <= 2012:
    generasi = "Generasi Z"
    keterangan = "Tumbuh langsung di dunia internet dan teknologi canggih (iGeneration), sangat terhubung secara digital."
elif 2013 <= tahun_lahir <= 2024:
    generasi = "Generasi Alpha"
    keterangan = "Generasi pertama yang sepenuhnya lahir di abad ke-21, sangat dipengaruhi teknologi cerdas sejak kecil."
elif 2025 <= tahun_lahir <= 2039:
    generasi = "Generasi Beta"
    keterangan = "Generasi mendatang yang diprediksi akan melanjutkan keterhubungan digital tingkat lanjut."
else:
    generasi = "Tidak Teridentifikasi"
    keterangan = "Tahun lahir yang dimasukkan berada di luar daftar generasi yang tersedia."

# hasil setelah pengecekan
print( )
print("HASIL PENGECEKAN TAHUN LAHIR")
print("Tahun Lahir:", tahun_lahir)
print("Generasi   :", generasi)
print("Keterangan :", keterangan)
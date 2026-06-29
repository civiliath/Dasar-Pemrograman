# Program: Implementasi Parameter Dinamis (*args dan **kwargs)

# 1. Parameter dinamis berupa List menggunakan tanda (*)
def daftar_file_csv(*nama_file):
    print("Daftar file CSV yang diunggah:")
    # Melakukan looping untuk menampilkan setiap item di dalam list
    for file in nama_file:
        print("-", file)
    print() # Baris kosong untuk pemisah

# 2. Parameter dinamis berupa Dictionary menggunakan tanda (**)
def gaya_elemen_css(**style):
    print("Properti CSS yang diterapkan:")
    # Melakukan looping untuk mengambil kunci (key) dan nilai (value) dari dictionary
    for properti, nilai in style.items():
        print(f"{properti}: {nilai}")

# Memanggil function parameter dinamis list dengan jumlah argument bebas
daftar_file_csv("data_mentah.csv", "data_bersih.csv", "hasil_spk.csv")

# Memanggil function parameter dinamis dictionary dengan format key=value
gaya_elemen_css(background_color="black", color="red", font_weight="bold")
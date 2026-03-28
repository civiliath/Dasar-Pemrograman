# Latihan 1.2 Input Tipe Data dan Variabels

# Input data dari user
nama_game = str(input("Apa nama gamenya? "))
developer = str(input("Siapa developernya? "))
genre = str(input("Apa genrenya? "))
rating = float(input("Berapa ratingnya? (contoh: 4.8) "))
jumlah_karakter = int(input("Berapa jumlah karakternya? "))
game_online = bool(input("Apa termasuk dalam game online? "))

if game_online == "True":
    game_online = True
else:
    game_online = False

print(type(nama_game))
print(type(developer))
print(type(genre))
print(type(rating))
print(type(jumlah_karakter))
print(type(game_online))

print("Nama Game:", nama_game)
print("Developer:", developer)
print("Game ini memiliki genre", genre)
print("Ratingnya di Playstore adalah", rating)
print("Per Maret 2026 memiliki", jumlah_karakter, "karakter yang dapat dimainkan")
print("Termasuk dalam game online?", game_online)
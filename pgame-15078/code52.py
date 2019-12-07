#latihan code 5.2 : Tuple


#buat variabel
buah=("Durian", "Mangga", "Rambutan")

print(buah)
print(type(buah))

print("Jumlah Element :", len(buah))

#tambah elemen yang sama
# buah.append("Mangga")
# print("Jumlah Buah Mangga :", buah.count("Mangga"))

#buah tuple dalam tuple
buah=('Durian', 'Mangga', 'Rambutan', 'Mangga', 'Salak', 
	('Nangka', 'Apel'))

print("Bauah [-1][0] :", buah[-1][0])

#mengubah elemen tuple
x_buah = list(buah)
x_buah[0] = "Melon"
Buah = tuple(x_buah)

print("Tuple :", buah)

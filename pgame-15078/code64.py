#latihan code 6.4 : Perulangan (Loop) for
batas='*'*30

#contoh 1
loyang = ["Apel", "Pisang", "Durian", "Melon"]
for buah in loyang:
	print(buah)

#contoh 2
print(batas)
for x in range(5):
	print("Halo Anak Info")
#	print(x)

# #contoh 3 (syntax 'end' error)
# print(batas)
# jumlah = 5
# teks = "Informatika"
# for x in range(jumlah):
# 	print(teks, end=',')

#contoh 4
print(batas)
for buah in loyang:
	print(buah)
	if buah == "Pisang":
		break

print(batas)
#contoh 5
for x in range(10,0,-1):
	print(x)

print(batas)
#contoh 6
for x in range(10,0,-2):
	print(x)

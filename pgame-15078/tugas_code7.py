#buat fungsi dapat mencetak nama sebanyak 5 kali
#gunakan while dan for
#buat fungsi perkalian

#menggunakan while
batas='*'*30
nama = 0
while (nama < 5):
	# x = x + 1
	nama += 1
	print("Nama : Frangki Nanangkong.", nama)
print(batas)

#menggunakan for
print(batas)
for x in range(5):
	print("Frangki Nanangkong")

#buat fungsi  perkalian, pembagian, dan pangkat
print(batas)
a = input("Inputkan nilai a:")
b = input("Inputkan nilai b:")

#operator penjumlahan
c = a + b
print "Hasil %d + %d = %d" % (a,b,c)
#operator pengurangan
c = a - b
print "Hasil %d - %d = %d" % (a,b,c)
#operator perkalian
c = a * b
print "Hasil %d * %d = %d" % (a,b,c)
#operator pembagian
c = a / b
print "Hasil %d / %d = %d" % (a,b,c)
#operator pangkat
c = a ** b
print "Hasil %d ** %d = %d" % (a,b,c)

print(batas)



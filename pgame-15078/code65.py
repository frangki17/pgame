#latihan code 6.5 : Fungsi / Fucntion

#Contoh fungsi 1, nama fungsi : myfungsi
def myfungsi():
	print("Ini dicetak dari myfungsi")

#Contoh fungsi 2, nama fungsi : my_fungsi
def my_fungsi():
	print("Ini dicetak dari my_fungsi")

#contoh fungsi 3, nama fungsi : tambah_1
def tambah_1():
	print("t1 :", 4+4)

#contoh fungsi 4, nama fungsi : tambah_2
def tambah_2():
	a=4
	b=4
	print("t2 :", a+b)

#contoh fungsi 5, menggunakan parameter
def cetak_kata(kata):
	print("Kata yang dicetak :", kata)

#memanggil fungsi, caranya :
#tulis nama fungsi diikuti dengan "()"

myfungsi()
my_fungsi()
tambah_1()
tambah_2()
#memanggil fungsi cetak_kata dengan parameter
cetak_kata("Hallo")



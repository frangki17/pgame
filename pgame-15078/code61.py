#pemrograman game praktikum 6
#kondisional lanjutan if, else, elif
#memeriksa variable dengan fungsi isnumeric()

#Buat variable untuk menampung inputan dari user
myvar=input("Masukan Numerik atau String : ")

#kondisional if, else
#memeriksa variable dengan fungsi "isnumeric()"
if myvar.isnumeric():
	print("C1 : Ya, Variable myvar Numerik : ", myvar)
else:
	pass
	#pass adalah perintah untuk abaikan

#print batas garis bintang
print('*'*25)

#kondisional if, elif
if not myvar.isnumeric():
	print("C2: Variable myvar BUKAN Numerik ! ")
elif myvar.isnumeric():
	print("C2: myvar : %s, adalah Numerik " % myvar)
	print("C2: myvar : "+ myvar + ", adalah Numerik")
	print("C2: myvar Numerik : ", myvar)


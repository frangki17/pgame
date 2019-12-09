#pemrograman game praktikum 6
#perulangan lanjutan (loop) while

batas='*'*30
#contoh 4
#penggunaan while dan else
c = 1
while c < 6:
	print("C ==",c)
	c += 1
else:
	print(batas)

#contoh 5
#penggunaan while dan list
buah = ["Apel", "Melon", "Durian"]
print("Buah 1: ", buah)
while buah:
	print("\tbuah: ",buah.pop())
print("Buah 2: ",buah)

print(batas)
#contoh 6
n = 10
while n > 0:
	print(n)
	n-= 1


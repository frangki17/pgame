#praktikum 6
#perulangan (loop) while


batas='*'*30
#contoh 1
x = 0
while (x < 5):
	# x = x + 1
	x += 1
	print("Praktikum 6 no.", x)

print(batas)

#kombinasi while if
a = 0
while a < 6:
	print(" no a == ", a)
	if a == 3:
		break
	a += 1

print(batas)

#kombinasi while, if dan continue
b = 0
while b < 6:
	b += 1
	if b == 3:
		print("B == ", b)
	continue
	print(b)

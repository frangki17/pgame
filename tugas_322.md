#Pengertian dan Fungsi Operator Bitwise
Operator Bitwise merupakan operator yang digunakan untuk memanipulasi data dalam bentuk bit.
###1.AND (&) adalah Output yang bernilai 0 apabila minimal salah satu dari input/bit yang dibandingkan bernilai 0. Output akan bernilai 1 apabila semua input/bit yang dibandingkan bernilai 1.
###2.OR(|) adalah output bernilai 1 apabila yang dibandingan bernilai 1. Output akan bernilai 0 apabila semua input/bit bernilai 0.
###3.XOR(^) adalah output yang bernilai 1 apabila input/bit benilai berlawanan (1-0)(0-1). Ouput bernilai 0 (0-0) atau (1-1).
###4.LeftShift(<<) operator ini digunakan untuk menggeser bit data ke kiri.
###5.RightShift(>>) operator ini digunakan untuk menggeser bit ke kanan.
###6.Negasi/kebalikan(~) operator ini digunakan menghindari semua bit.


```python
a=int(input("masukan nilai A="))
b=int(input("masukan nilai B=" ))

c= a & b
print("{} & {}={}". format(a,b,c))

c= a | b
print("{} | {}={}". format(a,b,c))

c= a ^ b
print("{} | {}={}". format(a,b,c))

c= ~a
print("~{}= {}". format(a,b,c))

c= a << b
print("{} << {}={}". format(a,b,c))

c=a >> b
print("{} >> {}={}". format(a,b,c))
```

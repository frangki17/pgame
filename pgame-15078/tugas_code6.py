#tugas code 6
#hitung nilai mahasiswa

nama = raw_input("Masukan Nama : ")
nim = input("Masukan NIM : ")
uts = input("Masukan Nilai UTS : ")
uas = input("Masukan Nilai UAS : ")
tugas = input("Masukan Nilai Tugas : ")

Uts=uts*40/100;
Uas=uas*40/100;
Tugas=tugas*20/100;
#rumus nilai akhir
nilai_akhir=Uts+Uas+Tugas;

#tampilan output nama dan nilai yg di input

print "\nNama : %s" %nama
print "NIM : %s" %nim
print "Nilai UTS : %d" %uts
print "Nilai UAS : %d" %uas
print "Nilai Tugas %d" %tugas
print "Nilai Akhir :",float(nilai_akhir)

#kondisi if

if nilai_akhir >=80 :
	print "\nNilai Huruf : A"
elif nilai_akhir >=70 :
	print "\nNilai Huruf : B"
elif nilai_akhir >=55 :
	print "\nNilai Huruf : C"
elif nilai_akhir >=40 :
	print "\nNilai Huruf : D"
elif nilai_akhir >=39 :
	print "\nNilai Huruf : E"

if nilai_akhir >=60 :
	print "Keterangan : LULUS"
else :
	print "Keterangan : TIDAK LULUS"



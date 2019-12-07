#buat variabel dan berikan nilai
prodi = "Teknik Informatika"
konsen = "Jaringan"
mata_kuliah = "Pemrograman Game"
kampus = "UMMU"
lokasi = "Ternate"
tahun = 2019

#menampilkan nilai variabel ke layar
print(prodi)
print(konsen)
print(mata_kuliah)
print(kampus)
print(lokasi)

#cetak '-' sebanyak 35 kali
print('*'*35)

#cetak nilai variabel ke layar dengan keterangan
print("Prodi : ", prodi)
print("Konsentrasi : ", konsen)
print("Mata Kuliah : ", mata_kuliah)
print("Kampus : %s " % kampus)
print("Lokasi : %s " % lokasi)
print("Tahun : %s " % tahun)

#cetak '-' sebanyak 35 kali
print('*'*35)

#cetak variabel prodi dan kampus
print("Prodi & Kampus : ", prodi, ",", kampus)
print("Prodi dan Kampus :", prodi + ", " + kampus)
print("Prodi dan Kampus : %s, %s " % (prodi, kampus))

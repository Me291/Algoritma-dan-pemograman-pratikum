"""
@materi : operasi aritmatika
@judul : Menghitung satuan panjang
@hari/tanggal : Senin, 20210927
@nim : 065002100022
@author : Muhammad Tegar Hidayatullah 
"""

import math 

angka1 = float(input("masukan angka pertama: "))
angka2 = float(input("masukan angka kedua: "))

penjumlahan = angka1 + angka2
print("hasil",angka1,"ditambah dengan",angka2,"adalah",penjumlahan)

pengurangan = angka1 - angka2
print("selisih",angka1,"dengan",angka2,"adalah",pengurangan)

perkalian = angka1 * angka2
print("perkalian",angka1,"dengan",angka2,"adalah",perkalian)

pembagian = perkalian % angka2 
print("sisa pembagian dari hasil",perkalian,"dibagi",angka2,"adalah",pembagian)

jumlah = angka1 / angka2
print("jumlah dari pembagian",angka1,"dengan",angka2,"adalah",jumlah)

logaritma = math.log10(angka1)
print("hasil log(a) adalah",angka1)

perpangkatan = angka1**angka2
print("hasil a pangkat b adalah",perpangkatan)




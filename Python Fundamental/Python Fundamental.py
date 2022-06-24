# Code Hello World
from cgi import print_arguments
import imp


print("Hello World")
print(5+1)

    # Tugas Praktek
    print(10*2+5)
    print("Academy DQLab")


# Comment pada Python
print("Ini adalah sebuah baris kode") #ini adalah cotoh comment dan tidak akan tercetak

    # Tugas Praktek
    print(10*2+5) #fungsi matematika
    print("Academy DQLab") #fungsi mencetak kalimat


# Printing Data Type
## Tipe Data Boolean
print(True)

## Tipe Data String
print("Ayo belajar Python")
print('Belajar Python sangat Mudah di DQLAB')

## Tipe Data Integer
print(20)

## Tipe Data Float
print(3.14)

## Tipe Data List
print([1,2,3,4,5])
print(["satu", "dua", "tiga"])

## Tipe Data Tuple
print((1,2,3,4,5))
print(("satu", "dua", "tiga"))

## Tipe Data Dictionary
print({"nama":"Budi", 'umur':20})

## Tipe Data Dictionary dimasukan ke dalam variabel biodata
biodata = {"nama":"Andi", 'umur':21} #proses inisialisasi variabel biodata
print(biodata) #proses pencetakan variabel biodata yang berisi tipe data Dictionary
type(biodata) #fungsi untuk mengecek jenis tipe data. akan tampil <class 'dict'>

    #Tugas Praktek
    var_string = "Belajar Python DQLAB"
    var_int = 10
    var_float = 3.14
    var_list = [1,2,3,4]
    var_tuple = ("satu", "dua", "tiga")
    var_dict = {"nama":"Ali", 'umur':20}

    print(var_string)
    print(var_int)
    print(var_float)
    print(var_list)
    print(var_tuple)
    print(var_dict)

    print(type(var_string))
    print(type(var_int))
    print(type(var_float))
    print(type(var_list))
    print(type(var_tuple))
    print(type(var_dict))


# IF Statement
i = 10 #inisialisasi variable i yang memiliki nilai 10
if(i==10): #pengecekan nilai i apakah sama dengan 10
    print("ini adalah angka 10") #jika TRUE maka akan mencetak kalimat ini


# IF ... ELSE ...
i = 10 #inisialisasi variable i yang memiliki nilai 10
if(i==10): #pengecekan nilai i apakah sama dengan 10
    print("ini adalah angka 10") #jika TRUE maka akan mencetak kalimat ini
else:
    print("bukan angka 10") #jika FALSE akan mencetak kalimat ini


# IF ... ELIF ... ELSE
i = 5
if(i==5):
    print("ini adalah angka 5")
elif(i>5):
    print("lebih besar dari 5")
else:
    print("lebih kecil dari 5")


# NESTED IF
i = 2
if(i<5):
    print("nilai i kurang dari 7")
if(i<3):
    print("nilai i kurang dari 7 dan kurang dari 3")
else:
    print("nilai i kurang dari 7 tapi lebih dari 3")


# Praktik Operasi Matematika
a = 10
b = 5
selisih = a-b
jumlah = a+b
kali = a*b
bagi = a/b

print("Hasil penjumlahan a dan b adalah", jumlah)
print("Selisih a dan b adalah:", selisih)
print("Hasil perkalian a dan b adalah:", kali)
print("Hasil pembagian a dan b adalah:", bagi)


# Operasi Modulus
c = 10
d = 3
modulus = c%d

print("Hasil modulus:", modulus)


# Tugas Mid Praktek
angka = 5
if(angka%2==0):
    print("Angka termasuk bilangan genap")
else:
    print("Angka termasuk bilangan ganjil")


# While
j = 0 #nilai awal j=0
while j<6: #ketika j kurang dari 6 lakukan perulangan, jika tidak stop perulangan
    print("Ini adalah perulangan ke -", j) #lakukan perintah ini ketika perulangan
    j = j+1 #setiap kali diakhir perulangan update nilai dengan ditambah 1


# For (1)
for i in range (1,6): #perulangan for sebagai inisialisasi dari angka 1 hingga anka yang lebih kecil daripada 6.
    print("Ini adalah perulangan ke -", i) #perintahjika looping akan tetap berjalan


# For (2)
for i in range (1,11):
    if(i%2==0):
        print("Angka Genap", i)
    else:
        print("Angka Ganjil", i)


# Membuat Fungsi
def salam():
    print("Helo, Selamat Pagi")
## Pemanggilan Fungsi
salam()


# Parameter pada Fungsi
def luas_segitiga(alas, tinggi): #alas dan tinggi merupakan parameter yang masuk
    luas = (alas * tinggi) / 2
    print("Luas segitiga: %f" % luas);

# Pemanggilan Fungsi
## 4 dan 6 merupakan parameter yang diinputkan kedalam fungsi luas segitiga
luas_segitiga(4, 6)


# Fungsi dengan Return Value
def luas_segitiga(alas, tinggi): #alas dan tinggi merupakan parameter yang masuk
    luas = (alas * tinggi) / 2
    return luas

# Pemanggilan Fungsi
## 4 dan 6 merupakan parameter yang diinputkan kedalam fungsi luas segitiga
print("Luas segitiga: %d" % luas_segitiga(4, 6))


# Import Package dan Menggunakan Modul
import math
print("Nilai pi adalah:", math.pi) #math.pi merupakan sintak untuk memanggil fungsi


# Import dengan Module Rename atau Alias
import math as m #menggunakan m sebagai module rename atau alias
print("Nilai pi adalah:", m.pi) #m.pi merupakan sintak untuk memanggil fungsi


# Import sebagai Fungsi
from math import pi
print("Nilai pi adalah", pi)


# Import Semua Isi Moduls
from math import *
print("Nilai e adalah:", e)


# Membaca Teks File (CSV)
import requests
from contextlib import closing
import csv

# tentukan lokasi file, nama file, dan inisialisasi csv
url = 'https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv'

# baca file csv secara streaming
with closing(requests.get(url, stream=True)) as r:
	f = (line.decode('utf-8') for line in r.iter_lines())
	reader = csv.reader(f, delimiter=',')

# membaca baris per baris
for row in reader:
    print (row)


# Membaca File CSV dengan Menggunakan PANDAS

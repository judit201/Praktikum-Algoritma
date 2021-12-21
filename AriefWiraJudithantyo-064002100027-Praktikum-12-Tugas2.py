print("Program untuk membuat file Mean dan Standar deviasi ")

judul = str(input("Masukkan nama file : "))
filename = (f"{judul}.csv")
f = open(filename, "w")
f.close()
print(f"File {filename} telah dibuat")
print("TEKAN F atau F untuk menghentikan program")
print("===============================================")

file = open('Negara.csv','r')

class my_dictionary(dict):

    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

data = my_dictionary()
c1 = []
c2 = []
c3 = []
c4 = []
c5 = []

x = 0
for delimiter in file:
    x += 1
    delimiter = delimiter.split(',')
    if x == 1:
        pass
    else:
        p1 = delimiter[0]
        c1.append(p1)
        p2 = delimiter[1]
        c2.append(p2)
        p3 = delimiter[2]
        c3.append(p3)
        p4 = int(delimiter[3])
        c4.append(p4)
        p5 = int(delimiter[4])
        c5.append(p5)

data.add('Negara',c1)
data.add("Ibu Kota",c2)
data.add('Benua',c3)
data.add('Luas',c4)
data.add('Populasi',c5)

import pandas as pd

def write(string):
    file = open(f"{judul}.csv","w")
    file.write(str(string))
    file.close()

def read():
    file = open(f"{judul}.csv", "r")
    teks = file.read()
    print(teks)

baris = True
while baris == True:
    hasil = pd.DataFrame(data)
    print("\n Data dan Luas Negara di Dunia \n\n", hasil)
    print("Masukkan 0 untuk menyimpan file")
    print("Masukkan 1 untuk mencari dan menulis file mean")
    print("Masukkan 2 untuk mencari dan menulis file std ")

    isi = int(input("Masukan pilihan:"))
    mean = hasil.groupby(['Benua']).mean()
    std = hasil.groupby(['Benua']).std()
    if isi == 0:
        print("\nteks telah tersimpan")
        baris = False
    elif isi == 1:
        print('\nRata rata :\n',mean)
        write(mean)
        read()
    elif isi == 2:
        print('\nStandar Deviasi :\n',std)
        write(std)
        read()

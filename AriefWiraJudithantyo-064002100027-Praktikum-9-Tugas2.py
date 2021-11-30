print("Program membuat file")
print(35*"-")

title = str(input("Masukkan nilai mahasiswa : "))
filename = (f"{title}.txt")
f = open(filename, "w")
f.close()

print(35*"-")
print(f"File {filename} telah dibuat")
print("Tekan z atau 1 untuk menghentikan program")
print(35*"-")

def write(string):
    file = open(f"{title}.txt","w")
    file.write(str(string))
    file.close()

def read ():
    file = open(f"{title}.txt", "r")
    teks = file.read()
    print(teks)
baris = True

while baris == True:
    isi = (input(""))
    if isi == "z" or isi == "1":
        print("\nTeks telah disimpan")
        baris = False
    else:
        write(isi)
        read()
        

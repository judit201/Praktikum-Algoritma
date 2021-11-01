def nilai_siswa ():
    nilai = 0    
    ulang = 1
    nomor = 0
    while ulang == 1:
        nomor += 1
        x = str(input("Tekan ENTER untuk mencari nilai rata-rata!\nNilai siswa: "))
        if x == '': 
            nomor -= 1
            ulang = 0
        else:
            if x == "A": 
                nilai += float(4.00)
                b = "4"
            elif x == "A-":
                nilai += float(3.75)
                b = "3,75"
            elif x == "B+":
                nilai += float(3.50)
                b = "3,5"
            elif x == "B":
                nilai += float(3.00)
                b = "3"
            elif x == "B-":
                nilai += float(2.75)
                b = "2,75"
            elif x == "C+":
                nilai += float(2.50)
                b = "2,5"
            elif x == "C":
                nilai += float(2.00)
                b = "2"
            elif x == "C-":
                nilai += float(1.75)
                b = "1,75"
            elif x == "D":
                nilai += float(1.50)
                b = "1,50"
            elif x == "E":
                nilai += float(1.25)
                b = "1,25"
            else:
                nomor -= 1
                b = "Masukkan nilai yang benar"
            print(f"Nilai ke-{nomor} = {b}")
    rata2 = nilai / nomor
    return rata2

print("Rata rata nilai adalah", nilai_siswa())

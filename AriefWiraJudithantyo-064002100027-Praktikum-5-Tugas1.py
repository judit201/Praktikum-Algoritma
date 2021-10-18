nilai = 0
nsiswa = list()

ulangi = 0
nomor = 0
while ulangi == 0:
    nomor += 1
    x = str(input('Ketik "exit" untuk mengakhiri program\nMasukkan nilai: '))
    if x == "exit":
        ulangi = 1
    else:
        if x == "A": 
            nilai = float(4.00)
        elif x == "A-":
            nilai = float(3.75)
        elif x == "B+":
            nilai = float(3.50)
        elif x == "B":
            nilai = float(3.00)
        elif x == "B-":
            nilai = float(2.75)
        elif x == "C+":
            nilai = float(2.50)
        elif x == "C":
            nilai = float(2.00)
        elif x == "C-":
            nilai = float(1.75)
        elif x == "D":
            nilai = float(1.50)
        elif x == "E":
            nilai = float(1.25)
        else:
            print("Masukkan nilai yang benar")
            nilai = 0
        print(('\nNilai ke-{0} = {1}').format(nomor,nilai))
        nsiswa.append(nilai)
    
rata2 = sum(nsiswa) / len(nsiswa) 
print("Rata - rata nya adalah", rata2)

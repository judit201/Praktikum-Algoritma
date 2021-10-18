print("Program ini akan menentukan jumlah hari dalam bulan tertentu ")
ulang = True
while ulang == True:
    print("Masukkan -1 untuk menghentikan program")
    bulan = int(input("Masukkan bulan (1-12): "))
    if bulan == -1:
        ulang = False
        print("Terima kasih!")
    else:
        if bulan == 1 or bulan == 2 or bulan == 3 or bulan == 4 or bulan == 5 or bulan == 6 or bulan == 7 or bulan == 8 or bulan == 9 or bulan == 10 or bulan == 11 or bulan == 12:
            if bulan == 2:
                tahun = int(input("Masukkan tahun (contoh, 2021) : "))
                if (tahun % 4 == 0):
                    print("Ada 29 hari dalam sebulan")
                else:
                    print("Ada 28 hari dalam sebulan")
            else:
                if bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12:
                    print("Ada 31 hari dalam sebulan")
                else:
                    print("Ada 30 hari dalam sebulan")
        else:
            print("* nilai yang dimasukan tidak valid:", bulan, "*")

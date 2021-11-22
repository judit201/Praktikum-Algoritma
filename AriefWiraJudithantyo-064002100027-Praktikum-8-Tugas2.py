def pemangkatan(bilangan, pangkat):
    if pangkat == 0:
        return 1
    elif pangkat < 0:
        return 1 / pemangkatan(bilangan, -pangkat)
    else:
        return bilangan * pemangkatan(bilangan, pangkat-1)

while True:
    bilangan = int(input("Masukkan angka : "))
    pangkat = int(input("Masukkan pangkat : "))
    print(pemangkatan(bilangan, pangkat))

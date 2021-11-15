def OrdinalNumber(a):
    while angka !=0:
        if (angka==1):
            return str(angka) + "st"
        if (angka==2):
            return str(angka) + "nd"
        if (angka==3):
            return str(angka) + "rd"
        if angka in range(4,21):
            return str(angka) + "th"
        if (angka==21):
            return str (angka) + "st"
        if (angka==22):
            return str (angka) + "nd"
        if (angka==23):
            return str (angka) + "rd"
        if (angka==24):
            return str(angka) + "th"
        if (angka==25):
            return str(angka) + "th"
        else:
            print("Invalid")

angka = int(input("Masukkan angka : "))
print(OrdinalNumber(angka))

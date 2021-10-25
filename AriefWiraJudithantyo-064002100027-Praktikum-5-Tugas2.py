total = 0
while True:
    try:
        umur = int(input("Masukkan umur : "))
    except ValueError:
        break
    if umur <= 2:
            print("Gratis")
    elif umur in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            total += 14.00
            print("Harga $14.00")
            print(f"Running total : ${total:.2f}")
    elif umur >= 65:
            total += 18.00
            print("Harga $18.00")
            print(f"Running total : ${total:.2f}")
    else:
            total += 23.00
            print("Harga $23.00")
            print(f"Running total : ${total:.2f}")
            
uang = float(input("Masukkan jumlah uang : "))
if uang > total:
    bayar = uang - total
    print(f"Running kembalian : ${bayar:.2f}")
elif uang < total:
    bayar = total - uang
    print(f"Maaf uang anda kurang ${bayar:.2f}")
else:
    print("Uang anda pas, Terimakasih!")

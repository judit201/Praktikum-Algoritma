def fib(x):
    if x <= 1:
        return x
    else:
        return(fib(x-1) + fib(x-2)) 

def cetak(y):
    if y <= 0:
        print("Angka positif")
    else:
        print("Bilangan fibonacci ke- " + str(y), "adalah",fib(y))

while True:
    try:
        bilangan = int(input("Masukkan bilangan : "))
    except ValueError:
        print("Invalid input, masukkan angka bulat!\n")
    else:
        cetak(bilangan)

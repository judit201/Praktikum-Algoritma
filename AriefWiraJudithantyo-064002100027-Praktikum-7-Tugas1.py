def cekBilangan(bil):
    if bil == 1:
        print(f"Bilangan ini {bil} adalah bilangan prima")
    elif bil == 2:
        print(f"Bilangan ini {bil} adalah bilangan prima")
    else:
        global x 
        for x in range(2, bil):
            if bil % x == 0:
                stat = 0 
                break
            else:
                stat = 1 
        cekstat(stat)
        
def cekstat(stat):
    if stat == 0:
        print(f"Bilangan ini {bil} adalah bilangan prima")
        print(f"{x} kali {bil//x} = {bil}")
    else:
        print(f"{bil} adalah bilangan prima")

a = 1
while a == 1:                    
    bil = int(input("Masukkan bilangan : "))
    cekBilangan(bil)                 
bil = int(input("Masukkan bilangan : "))
cekBilangan(bil)

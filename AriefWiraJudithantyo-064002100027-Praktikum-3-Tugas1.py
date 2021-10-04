print(20*"-")
a = int(input("Masukan sisi A = "))
b = int(input("Masukan sisi B = "))
c = int(input("Masukan sisi C = "))
print(20*"-")

if a == b == c :
    print("Segitiga Sama Sisi")
elif (a + b <= c) or (a + b <= c) or (a + b <= c) :
    print("Bukan Segitiga")
elif (a == b) or (a == c) or (b == c):
    print("Segitiga Sama Kaki")
elif (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a) :
    print("Segitiga Siku-siku")
else :
    print("Segitiga Sembarang")
print(20*"-")

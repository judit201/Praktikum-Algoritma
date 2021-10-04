from math import *
import math


print(43*"-")
print("Kalkulator Jarak Latitude dan Longitude")
print(43*"-")
lat1 = int(input("Masukkan Latitude  1  = "))
lat2 = int(input("Masukkan Latitude  2  = "))
lon1 = int(input("Masukkan Longitude 1  = "))
lon2 = int(input("Masukkan Longitude 2  = "))

lat1, lat2, lon1, lon2 = map(radians, [lat1, lat2, lon1, lon2])

dlat = lat2 - lat1
dlon = lon2 - lon1
a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
c = 2 * atan2(sqrt(a), sqrt(1-a))
radius = 6371
d = radius * c
print(43*">")
print(f"Jarak antara dua titik adalah {ceil(d)} kilometer")
print(43*">")
\

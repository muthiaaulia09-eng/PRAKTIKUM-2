import math

baris1 = input().split()

if len(baris1) >= 2:
    a = float(baris1[0])
    b = float(baris1[1])
else:
    a = float(baris1[0])
    b = float(input())
    
alas = math.sqrt((b ** 2) - (a ** 2))
tinggi = a
keliling = alas + tinggi + b
luas = 0.5 * alas * tinggi 

print(f"Alas = {int(alas)} cm")
print(f"Tinggi = {int(tinggi)} cm")
print(f"Keliling = {int(keliling)} cm")
print(f"Luas = {int(luas)} cm^2")
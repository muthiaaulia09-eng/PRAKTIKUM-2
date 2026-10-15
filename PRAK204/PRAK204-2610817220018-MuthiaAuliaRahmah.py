baris1 = input().split()

if len(baris1) >= 2:
    r = float(baris1[0])
    t = float(baris1[1])
else:
    r = float(baris1[0])
    t = float(input())

phi = 22.0 / 7.0
volume = phi * (r ** 2) * t
luas = 2 * phi * r * (r + t)
keliling = 2 * phi * r

print(f"Volume = {volume:.2f}")
print(f"Luas = {luas:.2f}")
print(f"Keliling = {keliling:.2f}")
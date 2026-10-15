import sys

input_data = []
for line in sys.stdin:
    if line.strip():  
        input_data.extend(line.split())
    if len(input_data) >= 6:  
        break

a, b, i, j, x, y = map(float, input_data)

hasil = (a - b) * i / j - (x + y)

print(f"{hasil:.3f}")
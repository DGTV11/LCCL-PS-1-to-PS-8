coords = list()
while True: 
    x = input("Please input an x coord (blank to stop): ")
    if x == str():
        break
    y = input("Please input a corresponding y coord: ")
    coords.append((float(x), float(y)))

sumxy = sumx = sumy = sumxsqr = 0

for x, y in coords:
    sumxy += x*y
    sumx += x
    sumy += y
    sumxsqr += x**2
n = len(coords)

m = (sumxy - ((sumx * sumy)/n))/(sumxsqr - (sumx**2)/n)
b = (sumy/n) - m*(sumx/n)

print(f'y ~ {m:.5f}x + {b:.5f}')
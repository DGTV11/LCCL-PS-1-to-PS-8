f = int(input('Feet: '))
i = float(input('Inches: '))
ti = i+(f*12)
c = round(ti*2.54, 2)

print(f'{f} feet and {i} inches is {c} centimeters')
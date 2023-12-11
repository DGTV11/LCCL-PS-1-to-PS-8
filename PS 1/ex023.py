import math

s = float(input('Length of each side: '))
n = float(input('Number of sides: '))

print(f'Area of the regular polygon with user-inputted parameters: {(n*(s**2))/(4*math.tan(math.pi/n))}')
import math
s1 = float(input('Length of side 1 of triangle: '))
s2 = float(input('Length of side 2 of triangle: '))
s3 = float(input('Length of side 3 of triangle: '))

s = (s1 + s2 + s3) / 2

print(f'Area of the triangle with user-inputted parameters: {math.sqrt(s * (s-s1) * (s-s2) * (s-s3))}')
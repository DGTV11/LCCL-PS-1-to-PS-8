'''
If you read the height in meters and the weight in kilograms 
then body mass index is computed using this slightly simpler formula:
BMI = weight/height^2
'''
h = float(input('Your height in meters: '))
w = float(input('Your weight in kilograms: '))

print(f'BMI: {w/h**2}')
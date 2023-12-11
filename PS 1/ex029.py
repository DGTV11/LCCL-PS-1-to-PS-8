'''
Write a program that begins by reading a temperature from the user in degrees Celsius. 
Then your program should display the equivalent temperature in degrees Fahrenheit and 
degrees Kelvin. The calculations needed to convert between different units of 
temperature can be found on the internet.
'''
c = float(input('Temprature in Degrees Celsius: '))
f = c * 9 / 5 + 32
k = c + 273.15
print(f'''
{c}°C
=
{f}°F
=
{k}K
''')
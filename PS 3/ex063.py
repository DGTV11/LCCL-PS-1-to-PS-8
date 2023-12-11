'''
Write a program that displays a temperature conversion 
table for degrees Celsius and degrees Fahrenheit. 
The table should include rows for all temperatures 
between 0 and 100 degrees Celsius that are multiples 
of 10 degrees Celsius. Include appropriate headings 
on your columns. The formula for converting between 
degrees Celsius and degrees Fahrenheit can be found 
on the internet.
'''

c2f = lambda n: int((n*1.8) + 32)

Celsius = list()
Fahrenheit = list()
for i in range(1,11):
    c = i*10
    Celsius.append(c)
    Fahrenheit.append(c2f(c))

print(f'''
Celsius || Fahrenheit
--------||-----------''')
for c, f in zip(Celsius, Fahrenheit):
    if c == 100:
        print(f'{c:}°C   || {f}°F')
    else:
        print(f'{c:}°C    || {f}°F')
'''
In this exercise, you will create a program that begins by reading a measurement in feet from the user. 
Then your program should display the equivalent distance in inches, yards and miles. Use the Internet 
to look up the necessary conversion factors if you don’t have them memorized.
'''

# DEFINE CONSTANTS
MILE = 63360
YARD = 36
INCH = 12

# BEGIN PROGRAM
f = float(input('Please input the amount of feet: '))

print(f"{f} feet is;\n")
## Inches
n = f * INCH
print(f'{n} inches')

## Yards
n = f / YARD
print(f'{n} yards')

## Miles
n = f / MILE
print(f'{n} miles')
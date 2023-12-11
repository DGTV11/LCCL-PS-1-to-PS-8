'''
The volume of a cylinder can be computed by multiplying the area of its circular base by its height. 
Write a program that reads the radius of the cylinder, along with its height, from the user and computes its volume. 
Display the result rounded to one decimal place.
'''
import math

r = float(input('Radius of the cylinder: '))
h = float(input('Height of the cylinder: '))

bA = math.pi*(r**2)

print(f'Volume of the cylinder with user-inputted parameters: {bA*h:.1f}')
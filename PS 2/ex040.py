'''
A triangle can be classified based on the lengths of its sides as equilateral, 
isosceles or scalene. All 3 sides of an equilateral triangle have the same length.
An isosceles triangle has two sides that are the same length, and a third side 
that is a different length. If all of the sides have different lengths then the 
triangle is scalene. Write a program that reads the lengths of 3 sides of a 
triangle from the user. Display a message indicating the type of the triangle.
'''

sides = list()
Type = str()

for i in range(3):
    sides.append(int(input("Please input a triangle side length: ")))
Sides = set(sides)

if len(Sides) == 1:
    Type = "equilateral"
elif len(Sides) == 2:
    Type = "isosceles"
elif len(Sides) == 3:
    Type = "scalene"

print(f'A triangle with side lengths {sides} is a {Type} triangle.')
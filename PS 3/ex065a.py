'''
Write a program that computes the perimeter of a 
polygon. Begin by reading the x and y values for 
the first point on the perimeter of the polygon 
from the user. Then continue reading pairs of x 
and y values until the user enters a blank line 
for the x-coordinate. Each time you read an 
additional coordinate you should compute the 
distance to the previous point and add it to the 
perimeter. When a blank line is entered for the 
x-coordinate your program should add the distance 
from the last point back to the first point to the 
perimeter. Then it should display the total 
perimeter. Sample input and output is shown below, 
with user input shown in bold:

Enter the x part of the coordinate: 0
Enter the y part of the coordinate: 0
Enter the x part of the coordinate: (blank to quit): 1
Enter the y part of the coordinate: 0
Enter the x part of the coordinate: (blank to quit): 0
Enter the y part of the coordinate: 1
Enter the x part of the coordinate: (blank to quit):

The perimeter of that polygon is 3.414213562373095
'''
import math
# Input block VVV
coords = list()
xy = list()
xy.append(int(input('Enter the x part of the coordinate: ')))
xy.append(int(input('Enter the y part of the coordinate: ')))
coords.append(xy)

while True:
    xy = list()
    x = input('Enter the x part of the coordinate: (blank to quit): ')
    if x == '':
        coords.append(coords[0])
        break
    xy.append(int(x))
    xy.append(int(input('Enter the y part of the coordinate: ')))
    coords.append(xy)

# Perimeter calculation block VVV
prevX = coords[0][0]
prevY = coords[0][1]
perimeter = 0

for item in coords:
    x = item[0]
    y = item[1]

    xdiff = abs(prevX-x)
    ydiff = abs(prevY-y)

    perimeter += math.sqrt((xdiff**2) + (ydiff**2))

    prevX = item[0]
    prevY = item[1]

# Output block VVV
print(f'The perimeter of that polygon is {perimeter}')
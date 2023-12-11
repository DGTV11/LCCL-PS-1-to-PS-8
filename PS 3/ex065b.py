import math

exit = False
perimeter = 0

# Input and calculation block VVV
x = int(input('Enter the x part of the coordinate: '))
y = int(input('Enter the y part of the coordinate: '))
firstxy = (x, y)
prevX = x
prevY = y

while True:
    x = input('Enter the x part of the coordinate: (blank to quit): ')

    if x == '':
        x = firstxy[0]
        y = firstxy[1]
        exit = True
    else:
        x = int(x)
        y = int(input('Enter the y part of the coordinate: '))

    xdiff = abs(prevX-x)
    ydiff = abs(prevY-y)

    perimeter += math.sqrt((xdiff**2) + (ydiff**2))

    prevX = x
    prevY = y

    if exit == True:
        break

# Output block VVV
print(f'The perimeter of that polygon is {perimeter}')
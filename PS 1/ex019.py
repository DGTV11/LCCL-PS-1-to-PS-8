'''
Create a program that determines how quickly an object is traveling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0 m/s. You can use the formula
f = final velocity
i = inital velocity = 0 meters per second
a = acceleration due to gravity = 9.8 meters per second squared
d = distance

f = sqrt(i^2 + 2ad)
'''
import math

I = 0
A = 9.8
D = float(input('Distance between object height and ground in meters: '))

f = math.sqrt((I**2) + (2*A*D))

print(f'Velocity on impact: {f} meters per second.')
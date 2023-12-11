"""
Write a program that begins by reading a radius, r , from the user. The program will continue by computing 
and displaying the area of a circle with radius r and the volume of a sphere with radius r. Use the pi 
constant in the math module in your calculations.

----------------------------------------------------------------------------------------------------------
Hint: The area of a circle is computed using the formula area = πr^2. The volume of a sphere is computed 
using the formula volume = (4/3)πr^3.
----------------------------------------------------------------------------------------------------------
"""
import math

r = float(input('Please input a radius: '))

cA = math.pi*(r**2)
sV = (4/3)*math.pi*(r**3)

print(f"""
- The area of a circle with your inputted radius is {cA}
- The volume of a sphere with your inputted radius is {sV}
""")
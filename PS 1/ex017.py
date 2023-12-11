'''
The amount of energy required to increase the temperature of one gram of a material by one degree Celsius is the material’s 
specific heat capacity, C. The total amount of energy required to raise m grams of a material by ΔT degrees Celsius can be
computed using the formula:
q = mCΔT
Write a program that reads the mass of some water and the temperature change from the user. Your program should display the 
total amount of energy that must be added or removed to achieve the desired temperature change.

-------------------------------------------------------------------------------------------------------------------------------------------
Hint: The specific heat capacity of water is 4.186 (Joule per g◦C). Because water has a density of 1.0 gram per millilitre, you can 
use grams and millilitres interchangeably in this exercise.
-------------------------------------------------------------------------------------------------------------------------------------------

Extend your program so that it also computes the cost of heating the water. Electricity is normally billed using units of
kilowatt hours rather than Joules. In this exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour (Canadian rate). 
Use your program to compute the cost of boiling water for a cup of coffee.

-------------------------------------------------------------------------------------------------------------------------------------------
Hint: You will need to look up the factor for converting between Joules and kilowatt hours to complete the last part of this exercise.
-------------------------------------------------------------------------------------------------------------------------------------------
'''

C = 4.186
KWH_COST = 0.2413 #24.13 cents (Singaporian rate)
m = float(input('Mass of water in grams: '))
ΔT = float(input('Temprature change in degrees Celsius: '))
j = m*C*ΔT
print(f'Energy required: {j} joules')

kWh = j/3600000
cost = kWh * KWH_COST
print(f'Cost of boiling water for a cup of coffee with user-inputted parameters: ${cost:.2f}')
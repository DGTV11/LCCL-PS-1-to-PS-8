'''
A roulette wheel has 38 spaces on it. 
Of these spaces, 18 are black, 18 are red, and 
two are green. The green spaces are numbered 0 
and 00. The red spaces are numbered 1,3, 5, 7, 9,
12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 
and 36. The remaining integers between 1 and 36 
are used to number the black spaces. Many 
different bets can be placed in roulette. We 
will only consider the following subset of them 
in this exercise:

•Single number (1 to 36, 0, or 00)
•Red versus Black
•Odd versus Even 
(Note that 0 and 00 do not pay out for even)
•1 to 18 versus 19 to 36

Write a program that simulates a spin of a 
roulette wheel by using Python’s random number 
generator. Display the number that was selected 
and all of the bets that mustbe payed. 
For example, if 13 is selected then your program 
should display:

The spin resulted in 13...
Pay 13
Pay Black
Pay Odd
Pay 1 to 18

If the simulation results in 0 or 00 then your 
program should display Pay 0 or Pay 00 without 
any further output.
'''
from random import randint

def iseven(n):
    return n % 2 == 0

GREEN = ['0', '00'] # 0, 00
RED = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
#Remaining is BLACK
number = randint(1, 38)
if number == 37:
    number = '0'
elif number == 38:
    number = '00'

print(f'The spin resulted in {number}...')

# Green
if number in GREEN:
    print(f'Pay {number}')
    quit()

# Single number
print(f'Pay {number}')

# Red VS Black
if number in RED:
    print('Pay Red')
else:
    print('Pay Black')

# Odd VS Even
if iseven(number):
    print('Pay Even')
else:
    print('Pay Odd')

# 1-18 VS 19-36
if number >= 1 and number <= 18:
    print('Pay 1 to 18')
else:
    print('Pay 19 to 36')
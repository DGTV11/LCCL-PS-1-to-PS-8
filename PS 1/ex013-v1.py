'''
Consider the software that runs on a self-checkout machine. One task that it must be able to perform is to 
determine how much change to provide when the shopper pays for a purchase with cash.
Write a program that begins by reading a number of cents from the user as an integer. Then your program should compute
and display the denominations of the coins that should be used to give that amount of change to the shopper. 
The change should be given using as few coins as possible. Assume that the machine is loaded with pennies, 
nickels, dimes, quarters, loonies and toonies.

----------------------------------------------------------------------------------------------------------------------
A one dollar coin was introduced in Canada in 1987. It is referred to as a loonie because one side of the coin has a 
loon (a type of bird) on it. The two dollar coin, referred to as a toonie, was introduced 9 years later. It’s name is 
derived from the combination of the number two and the name of the loonie.
----------------------------------------------------------------------------------------------------------------------
'''

'''
Pennies - 1c
Nickels - 5c
Dime - 10c
Quarter - 25c
Loonie - $1 - 100c
Toonie - $2 - 200c
'''

# DEFINE CONSTANTS
TOONIE = 200
LOONIE = 100
QUARTER = 25
DIME = 10
NICKEL = 5
PENNY = 1

# BEGIN PROGRAM
c = round(float(input('Please input the change in dollars: $')), 2)
c = round(c*100, 0)

print('Denominations of %sc'%str(c))

## Toonies
x = 0
i = 0
while x < c:
    i += 1
    x = TOONIE * i

if x > c:
    tc = i-1
elif x == c:
    tc = i
elif int(c) == 0:
    tc = 0

print('TOONIES - $2.00 × %s'%str(tc))
c -= TOONIE * tc

## Loonies
x = 0
i = 0
while x < c:
    i += 1
    x = LOONIE * i

if x > c:
    tc = i-1
elif x == c:
    tc = i
elif int(c) == 0:
    tc = 0

print('LOONIES - $1.00 × %s'%str(tc))
c -= LOONIE * tc

## Quarters
x = 0
i = 0
while x < c:
    i += 1
    x = QUARTER * i

if x > c:
    tc = i-1
elif x == c:
    tc = i
elif int(c) == 0:
    tc = 0

print('QUARTERS - $0.25 × %s'%str(tc))
c -= QUARTER * tc

## Dimes
x = 0
i = 0
while x < c:
    i += 1
    x = DIME * i

if x > c:
    tc = i-1
elif x == c:
    tc = i
elif int(c) == 0:
    tc = 0

print('DIMES - $0.10 × %s'%str(tc))
c -= DIME * tc

## Nickels
x = 0
i = 0
while x < c:
    i += 1
    x = NICKEL * i

if x > c:
    tc = i-1
elif x == c:
    tc = i
elif int(c) == 0:
    tc = 0

print('NICKELS - $0.05 × %s'%str(tc))
c -= NICKEL * tc

## Pennies
x = 0
i = 0
while x < c:
    i += 1
    x = PENNY * i

if x > c:
    tc = i-1
elif x == c:
    tc = i
elif int(c) == 0:
    tc = 0

print('PENNIES - $0.01 × %s'%str(tc))
c -= PENNY * tc

print(f"DEBUG: {c}")
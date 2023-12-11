### NO LOOPS!!!

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
n = c // TOONIE
print('TOONIES - $2.00 × %s'%str(n))
c %= TOONIE

## Loonies
n = c // LOONIE
print('LOONIES - $1.00 × %s'%str(n))
c %= LOONIE

## Quarters
n = c // QUARTER
print('QUARTERS - $0.25 × %s'%str(n))
c %= QUARTER

## Dimes
n = c // DIME
print('DIMES - $0.10 × %s'%str(n))
c %= DIME

## Nickels
n = c // NICKEL
print('NICKELS - $0.10 × %s'%str(n))
c %= NICKEL

## Pennies
n = c // PENNY
print('PENNIES - $0.10 × %s'%str(n))
c %= PENNY

print(f"DEBUG: {c}")
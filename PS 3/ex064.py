"""
February 4, 2013 was the last day that pennies
were distributed by the Royal Canadian Mint. Now 
that pennies have been phased out retailers must 
adjust totals so that they are multiples of 5 
cents when they are paid for with cash (credit 
card and debit card transactions continue to be 
charged to the penny). While retailers have some 
freedom in how they do this, most choose to round 
to the closest nickel. Write a program that reads 
prices from the user until a blank line is entered.
Display the total cost of all the entered items on 
one line, followed by the amount due if the 
customer pays with cash on a second line. The 
amount due for a cash payment should be rounded to 
the nearest nickel. One way to compute the cash
payment amount is to begin by determining how many 
pennies would be needed to pay the total. Then 
compute the remainder when this number of pennies 
is divided by 5. Finally, adjust the total down 
if the remainder is less than 2.5. Otherwise 
adjust the total up. 
"""

# 1p = $0.01

# Input block VVV
print('Please enter the prices.')
prices = list()
while True:
    nprice = input('$')
    if nprice == "":
        break
    else:
        prices.append(round(float(nprice), 2))
# Total calculation block VVV
totalamt = 0
for item in prices:
    totalamt += item
# Conversion block VVV
amt_pennies = totalamt * 100
nickel_remainder = amt_pennies % 5
approx_nickels = int(totalamt / 0.05)
if nickel_remainder > 2.5:
    approx_nickels += 1
converted_total = approx_nickels*0.05

# Output block VVV

print(f'''
{"Total amt":10s}${totalamt: >7.2f}
{"Amt due":10s}${converted_total: >7.2f}
''')
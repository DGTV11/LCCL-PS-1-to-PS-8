'''
A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60 
percent. Write a program that begins by reading the number of loaves of day old 
bread being purchased from the user. Then your program should display the 
regular price for the bread, the discount because it is a day old, and the total
price. All of the values should be displayed using two decimal places, and the 
decimal points in all of the numbers should be aligned when reasonable values 
are entered by the user.
'''
NORM_PRICE = 3.49
DISC_PRICE = NORM_PRICE * (1 - 0.60)

amt_dob = int(input('Amount of day old bread to purchase: '))
dit_b_norm = amt_dob * NORM_PRICE
dit_b_disc = amt_dob * DISC_PRICE

print(f'''
SUB_TOTAL - ${dit_b_norm:.2f}
DISCOUNT - $60

TOTAL - ${dit_b_disc:.2f}
''')
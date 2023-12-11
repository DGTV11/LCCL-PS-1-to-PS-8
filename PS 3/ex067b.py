'''
2 yrs and below        - $0.00
Between 3 and 12 yrs   - $14.00
Between 13 and 64 yrs  - $23.00
65 yrs and above       - $18.00
'''
# Vars
between3and12yrs = 0
between13and64yrs = 0
aboveOrEqualTo65yrs = 0

# Input and Counting
while True:
    age = input('Enter a guest\'s age: (blank to quit): ')
    if age == '':
        break

    age = int(age)
    
    if 2 < age < 13:
        between3and12yrs += 1
    elif age < 65:
        between13and64yrs += 1
    else:
        aboveOrEqualTo65yrs += 1

# Calculation
total_cost = (between3and12yrs * 14) \
        + (between13and64yrs * 23) \
        + (aboveOrEqualTo65yrs * 18)

# Output
print(f'{"Cost":6s}${total_cost: >7.2f}')
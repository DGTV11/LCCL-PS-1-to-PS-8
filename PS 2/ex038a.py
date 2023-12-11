d30 = [
    'april',
    'june',
    'september',
    'november'
]

d31 = [
    'january',
    'march',
    'may',
    'july',
    'august',
    'october',
    'december'
]

month = input('Please input a month: ')

if month.lower() in d30:
    print(f'The month of {month.lower()} has 30 days!')

elif month.lower() in d31:
    print(f'The month of {month.lower()} has 31 days!')

elif month.lower() == 'february':
    print(f'The month of {month.lower()} has 28 or 29 days!')

else:
    raise TypeError('haha this is what happens if you don\'t read the instructions')
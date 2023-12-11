MONTH_DATA = {
    'january'   : '31 days',
    'febuary'   : '28 or 29 days',
    'march'     : '31 days',
    'april'     : '30 days',
    'may'       : '31 days',
    'june'      : '30 days',
    'july'	    : '31 days',
    'august'    : '31 days',
    'september' : '30 days',
    'october'   : '31 days',
    'november'	: '30 days',
    'december'	: '31 days'
}

month = input('Please input a month: ')
if month.lower() in MONTH_DATA.keys():
    print(f'The month of {month.lower()} has {MONTH_DATA[month]}!')
else:
    raise TypeError('haha this is what happens if you don\'t read the instructions')
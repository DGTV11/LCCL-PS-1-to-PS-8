HOLI_DATA = {
    'january 1'     :   'New year’s day',
    'july 1'        :   'Canada day',
    'december 25'   :   'Christmas day'
}

date = input('Please input a canadian national holiday that is FIXED: ')
if date.lower() in HOLI_DATA:
    print(f'The date {date} is {HOLI_DATA[date]} in Canada!')
else:
    raise TypeError('haha this is what happens if you don\'t read the instructions')
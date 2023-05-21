'''
The Chinese zodiac assigns animals to years in a 12 year 
cycle. One 12 year cycle is shown in the table below. 
The pattern repeats from there, with 2012 being another
year of the dragon, and 1999 being another year of the 
hare.

Write a program that reads a year from the user and 
displays the animal associated with that year. 
Your program should work correctly for any year greater 
than or equal to zero, not just the ones listed in the 
table.
'''

YR_DATA = {
    0 : 'Dragon',
    1 : 'Snake',
    2 : 'Horse',
    3 : 'Sheep',
    4 : 'Monkey',
    5 : 'Rooster',
    6 : 'Dog',
    7 : 'Pig',
    8 : 'Rat',
    9 : 'Ox',
    10 : 'Tiger',
    11 : 'Hare'
}

scalept = int(input('Please input a year THAT EXISTS: '))
# print(f'DEBUG: {list(scalept)}')


while True: 
    if (scalept - 2000)%12 in YR_DATA:
        print(f'The year {scalept} is the year of the {YR_DATA[(scalept - 2000)%12]}')
        quit()
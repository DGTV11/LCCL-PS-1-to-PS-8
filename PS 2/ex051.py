GRADE_DATA = {
    'A+'    : 4.0,
    'A'     : 4.0,
    'A-'    : 3.7,
    'B+'    : 3.3,
    'B'     : 3.0,
    'B-'    : 2.7,
    'C+'    : 2.3,
    'C'     : 2.0,
    'C-'    : 1.7,
    'D+'    : 1.3,
    'D'     : 1.0,
    'F'     : 0
}

lg = input('Please input a letter grade: ')
if lg.upper() in GRADE_DATA:
    print(f'The letter grade {lg} is {GRADE_DATA[lg.upper()]} grade points!')
else:
    raise TypeError('haha this is what happens if you don\'t read the instructions')
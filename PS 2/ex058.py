'''
Write a program that reads a date from the user 
and computes its immediate successor. For 
example, if the user enters values that represent
2013-11-18 then your program should display a
message indicating that the day immediately after
2013-11-18 is 2013-11-19. If the user enters 
values that represent 2013-11-30 then the program
should indicate that the next day is 2013-12-01.
If the user enters values that represent 
2013-12-31 then the program should indicate that
the next day is 2014-01-01. The date will be 
entered in numeric form with three separate 
input statements; one forthe year, one for the 
month, and one for the day. Ensure that your 
program works correctly for leap years.
'''

month_lasts = {
1   : 31,
2   : 28, 
3   : 31,
4   : 30,
5   : 31,
6   : 30,
7   : 31,
8   : 31,
9   : 30,
10  : 31,
11  : 30,
12  : 31,
}

inp = input('Please input a date in this format "YYYY-MM-DD" without the quotes: ')
date = inp.split('-')

#Start of value check block
if len(date) <= 2:
    raise ValueError
for item in date:
    if not item.isdigit():
        raise ValueError
#End of value check block

year = int(date[0])
month = int(date[1])
day = int(date[2])

# Leap handler
if (year%400 == 0 or year%4 == 0) and month == 2:
    if day == 28:
        print(f'Next day: {year}-2-29')
    elif day == 29:
        print(f'Next day: {year}-3-1')
# NYE handler
elif month == 12 and day == 31:
    print(f'Next day: {year+1}-1-1')
# Last day of month handler (Excluding Leaps (Never excluded NYE cause KeyError))
elif day == month_lasts[month]:
    print(f'Next day: {year}-{month+1}-1')
# Normal day handler
else:
    print(f'Next day: {year}-{month}-{day+1}')

'''
Last line of defence if all 
else detects no errors:


D
R
U
M
R
O
L
L

P
L
E
A
S
E
.
.
.

















Your common sense, DUH!
'''
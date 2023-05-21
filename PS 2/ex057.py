year = int(input('Year: '))
if year%400 == 0 or year%4 == 0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')
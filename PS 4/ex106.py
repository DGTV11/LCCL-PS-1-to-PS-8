from ex091 import isLeapYear

MONTH_DATA = {
    1   : 31,
    3   : 31,
    4   : 30,
    5   : 31,
    6   : 30,
    7	: 31,
    8   : 31,
    9   : 30,
    10  : 31,
    11	: 30,
    12	: 31
}

def lenOmonth(m, y):
    isLeap = isLeapYear(y)

    if m != 2:
        return MONTH_DATA[m]
    elif isLeap:
        return 29
    else:
        return 28
if __name__ == "__main__":
    month = int(input("Please input a month (1-12): "))
    year = int(input("Please input a year: "))
    print(f"Month {month} of year {year} is {lenOmonth(month, year)} days long.")
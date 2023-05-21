# Feb -> 2 -> Leap

MONTHLENGTHS = [
    0, 31, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
]

def isLeapYear(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            return False
        return True

def ordinalDate(d, m, y):
    isLeap = isLeapYear(y)
    days = 0

    for i in range(1, m):
        if i == 2:
            if isLeap:
                days += 29
            else:
                days += 28
        else:
            days += MONTHLENGTHS[i]

    days += d
    
    return days

if __name__ == '__main__':
    d = int(input('Please input the day: '))
    m = int(input('Please input the month: '))
    y = int(input('Please input the year: '))

    print(f"{d}/{m}/{y} is day {ordinalDate(d, m, y)} of year {y}")
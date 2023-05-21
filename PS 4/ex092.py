from ex091 import *
MONTHLENGTHS_GD = [
    0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
]
def gregorianDate(d, y):
    isLeap = isLeapYear(y)
    days = d
    m = 0
    i = 0
    d_de = 0
    de = 0
    
    while True:
        if i == 2:
            if isLeap:
                days -= 29
                d_de += 29
            else:
                days -= 28
                d_de += 28
        else:
            days -= MONTHLENGTHS_GD[m]
            d_de += MONTHLENGTHS_GD[m]
        
        if days <= 0:
            dd = d - de
            break
        else:
            de = d_de
            m += 1
            i += 1
    
    return [dd, m, y]

if __name__ == '__main__':
    '''
    Your program could compute the due date for a baby based on a 
    gestation period of 280 days
    '''
    d = int(input("Please input day of start of gestation: "))
    m = int(input("Please input month of start of gestation: "))
    y = int(input("Please input year of start of gestation: "))
    od = ordinalDate(d, m, y)
    odx = od + 280
    fy = y + (odx // 360)
    fd = odx % 360
    gd = gregorianDate(fd, fy)

    print(f"Due date of baby: {gd[0]}/{gd[1]}/{gd[2]}")
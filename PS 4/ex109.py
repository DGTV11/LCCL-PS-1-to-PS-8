from ex106 import lenOmonth

isMagic = lambda d, m, y: (d * m) == (y % 100)

if __name__ == '__main__':
    # 20th century -> 1/1/1901 to 31/12/2000
    print("Magic dates in the 20th century:")
    for y in range(1901, 2001):
        for m in range(1, 13):
            for d in range(1, lenOmonth(m, y)+1):
                if isMagic(d, m, y):
                    print(f"{d}/{m}/{y}")
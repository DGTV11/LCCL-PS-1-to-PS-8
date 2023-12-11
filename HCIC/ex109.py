# Find all magic dates in 1900 - 1999
import helpers
helpers.ready_import_outofdir('/Volumes/Data stuffs/Python/LCCL_Python2/PS 4/')
import ex106

for y in range(1900, 2000):
    for m in range(1, 13):
        for d in range(1, ex106.lenOmonth(m, y)+1):
            if d*m == y%100:
                print(f'{d}/{m}/{y}')

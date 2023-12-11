import sys

try:
    x = open(sys.argv[1], 'r')
    # e = x.readlines()[::-1][:10][::-1]
    e = x.readlines()[:-11:-1][::-1]
    x.close()
    for line in e[:-1]:
        print(line[:-1])
    print(e[-1])
except FileNotFoundError:
    print('ERROR: File not found')
except IndexError:
    print('ERROR: Not enough input (files)')
except NameError:
    pass
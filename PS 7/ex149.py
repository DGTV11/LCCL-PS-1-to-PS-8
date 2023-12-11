import sys

try:
    x = open(sys.argv[1], 'r')
    print(x.readlines()[:10])
    x.close()
except IndexError:
    print('ERROR: Not enough input (files)')
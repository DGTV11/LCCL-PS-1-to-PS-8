import sys
lines = list()
try:
    with open(sys.argv[1], 'r') as inf:
        with open(sys.argv[2], 'a') as outf:
            for i, line in enumerate(inf.readlines()):
                outf.write(f'{i} {line}')
except FileNotFoundError:
    print('ERROR: File not found')
except IndexError:
    print('ERROR: Not enough input (files)')
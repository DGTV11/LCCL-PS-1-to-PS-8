import sys
from collections import deque

try:
    x = open(sys.argv[1], 'r')
    last10 = deque()
    for line in x.readlines():
        last10.append(line)
        if len(last10) > 10:
            last10.popleft()
    x.close()
    for line in last10:
        print(line.strip())
except FileNotFoundError:
    print('ERROR: File not found')
except IndexError:
    print('ERROR: Not enough input (files)')
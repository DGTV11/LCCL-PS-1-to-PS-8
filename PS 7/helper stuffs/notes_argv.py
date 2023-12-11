# command line parameters

import sys

try:
    print(float(sys.argv[1]) + float(sys.argv[2])) # 'ALL HAIL JIGGLYPUFF | THE GREATEST POKEMON IN EXISTANCE!!!'
except:
    print('Not enough arguments')
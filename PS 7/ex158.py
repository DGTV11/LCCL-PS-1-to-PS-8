import sys

if len(sys.argv) != 3:
    raise IndexError(f'ERROR: Wrong amount of input (files) (2 files needed for input file and output file, {len(sys.argv)-1} given)')

with open(sys.argv[1], 'r') as inputf:
    with open(sys.argv[2], 'w') as outputf:
        for line in inputf.readlines():
            hasComment = False
            strstack = []
            for i, char in enumerate(line):
                if char in ('\'', '"'):
                    if len(strstack) > 0 and strstack[-1] == char:
                        strstack.pop()
                    else:
                        strstack.append(char)
                if char == '#' and not bool(strstack):
                    outputf.write(line[:i]+'\n')
                    hasComment = True
            if not hasComment:
                outputf.write(line)



import sys
lines = list()
for i, path in enumerate(sys.argv[1:]):
    try:
        f = open(path, 'r')
        e = f.readlines()
        for line in e[:-1]:
            lines.append(line[:-1])
        lines.append(e[-1])
        f.close()
    except FileNotFoundError:
        print('ERROR: File not found, proceeding to output' if i == len(sys.argv)-1 else 'ERROR: File not found, proceeding to next file')
    except IndexError:
        print('ERROR: Not enough input (files)')

print('Concatenated files:')
for line in lines:
    print(line)
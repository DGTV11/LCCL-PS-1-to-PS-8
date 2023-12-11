import sys
words = list()
maxlen = 0
maxlenwords = list()
try:
    f = open(sys.argv[1], 'r')
    for line in f:
        if not line.isspace():
            linewords = line.split()
            for word in linewords:
                words.append(word)
                if len(word) == maxlen:
                    maxlenwords.append(word)
                elif len(word) > maxlen:
                    maxlen = len(word)
                    maxlenwords = list()

    f.close()
except FileNotFoundError:
    print('ERROR: File not found')
except IndexError:
    print('ERROR: Not enough input (files)')

print(f'Length of longest word: {maxlen}\nLongest words:')
for word in maxlenwords:
    print(word)
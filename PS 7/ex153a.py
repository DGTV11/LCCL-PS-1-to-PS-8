import sys
lines = list()
try:
    f = open(sys.argv[1], 'r')
    for line in f:
        if not line.isspace():
            lines.append(line)
    f.close()
except FileNotFoundError:
    print('ERROR: File not found')
except IndexError:
    print('ERROR: Not enough input (files)')

words = list()
for line in lines:
    for word in line.split():
        words.append(word)

wordlens = list()
for word in words:
    wordlens.append(len(word))
maxlen = max(wordlens)

maxlenwords = list()
for word in words:
    if len(word) == maxlen:
        maxlenwords.append(word)

print(f'Length of longest word: {maxlen}\nLongest words:')
for word in maxlenwords:
    print(word)
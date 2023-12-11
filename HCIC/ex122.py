from ex117 import tokenise

VOWELS = ['a', 'e', 'i', 'o', 'u']
CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

def translate(tokens):
    outtoks = []
    for tok in tokens:
        if tok[0] in CONSONANTS:
            for i, char in enumerate(tok):
                if char in VOWELS:
                    i = i
                    break
            outtoks.append(tok[i:] + tok[:i] + 'ay')
        else:
            outtoks.append(tok + 'way')
    
    y = ''
    for tok in outtoks:
        y += tok + ' '
    return y

if __name__ == '__main__':
    print(translate(input('INPUT RAW ENGLISH THINGY TO TRANSLATE INTO SUPER SECRET TOTALLY NOT PIG LATIN!!! MUAHAHAHAHA: ')))
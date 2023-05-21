from ex122 import transWord

PUNCS = [".", ",", ":", ";", "?", "!", "'", "\""]

sentc = input("ORIGINAL TEXT: ")
nsentc = str()

for word in sentc.split():
    readybin = str()
    puncf = str()
    puncb = str()
    wordx = word
    
    e = 0
    while word[e] in PUNCS:
        e += 1

    f = -1
    while word[f] in PUNCS:
        f -= 1
    
    wordx = word[e:] if f == -1 else word[e:f+1]
    puncb = '' if f == -1 else word[f+1:]
    puncf = word[:e]

    # for e, c in enumerate(word):
    #     if c in PUNCS:
    #         puncf += c
    #     else:
    #         break
    # for f, c in enumerate(word[::-1]):
    #     if c in PUNCS:
    #         puncb = c + puncb
    #     else:
    #         break
    # if f == 0:
    #     wordx = wordx[e:]
    # else:
    #     wordx = wordx[e:-f]

    isCaps = wordx[0].isupper()
 
    readybin = transWord(wordx.lower())

    if isCaps:
        readybin = readybin.capitalize()
    
    readybin = puncf + readybin + puncb
        
    nsentc += readybin + " "

print(f"TRANSLATED TEXT: {nsentc}")
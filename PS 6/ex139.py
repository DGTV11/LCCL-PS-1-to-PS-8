import re

table = {
    'A':'.- ',
    'B':'-... ',
    'C':'-.-. ',
    'D':'-.. ',
    'E':'. ',
    'F':'..-. ',
    'G':'--. ',
    'H':'.... ',
    'I':'.. ',
    'J':'.--- ',
    'K':'-.- ',
    'L':'.-.. ',
    'M':'-- ',
    'N':'-. ',
    'O':'--- ',
    'P':'.--. ',
    'Q':'--.- ',
    'R':'.-. ',
    'S':'... ',
    'T':'- ',
    'U':'..- ',
    'V':'...- ',
    'W':'.-- ',
    'X':'-..- ',
    'Y':'-.-- ',
    'Z':'--.. ',
    '0':'----- ',
    '1':'.---- ',
    '2':'..--- ',
    '3':'...-- ',
    '4':'....- ',
    '5':'..... ',
    '6':'-.... ',
    '7':'--... ',
    '8':'---.. ',
    '9':'----. '
}

inseq = list(re.sub(r'\W+', '', input('Input words here: ').upper()))
outseq = str() # outseq = []
for char in inseq:
    outseq += table[char] # outseq.append(table[char])

print(outseq) # ''.join(outseq)
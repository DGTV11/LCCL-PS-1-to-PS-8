from string import punctuation

table = {ord(p):'' for p in punctuation+' '}
# table[' '] = ''
# table.update([(' ', ''))
# table.update({' ': ''})

w1 = sorted(list(input('Word 1: ').upper().translate(table)))
w2 = sorted(list(input('Word 2: ').upper().translate(table)))

print('Is an anagram' if w1 == w2 else 'Isn\'t an anagram!')
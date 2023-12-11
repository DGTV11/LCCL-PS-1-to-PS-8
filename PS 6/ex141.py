from ex136 import reverseLookup

number0to192word = {
    '00': 'zero',
    '01': 'one',
    '02': 'two',
    '03': 'three',
    '04': 'four',
    '05': 'five',
    '06': 'six',
    '07': 'seven',
    '08': 'eight',
    '09': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
}

number2Xto9X2word = {
    '2': 'twenty',
    '3': 'thirty',
    '4': 'forty',
    '5': 'fifty',
    '6': 'sixty',
    '7': 'seventy',
    '8': 'eighty',
    '9': 'ninety'
}


def num2word(x):
    outlist = list()

    if len(x) < 1 or len(x) > 3 :
        raise KeyError('Invalid number length!')
    elif not x.isnumeric():
        raise KeyError('Invalid characters!')
    if len(x) == 1:
        x = '0' + x

    if list(x)[-2]+list(x)[-1] in number0to192word.keys():
        outlist.insert(0, number0to192word[list(x)[-2]+list(x)[-1]])
    elif list(x)[-1] == '0' and list(x)[-2] != '0':
        outlist.insert(0, number2Xto9X2word[list(x)[-2]])
    elif list(x)[-1] != '0' and list(x)[-2] != '0':
        outlist.insert(0, number2Xto9X2word[list(x)[-2]]+' '+number0to192word['0'+list(x)[-1]])

    if len(x) == 3:
        outlist.insert(0, number0to192word['0' + x[0]]+' hundred')

    xx = str()
    for item in outlist:
        xx += item + ' '
    return xx

print('TEST 1:')
for i in range(0, 1000):
    print(f'{i} in words: {num2word(str(i))}')

print('TEST 2:')
x = input('Number between 0 and 999: ')    
print(f'Number in words: {num2word(x)}')
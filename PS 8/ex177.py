'''
As the name implies, Roman numerals were developed in ancient Rome. Even after the Roman empire fell, its numerals continued to be widely 
used in Europe until the late middle ages, and its numerals are still used in limited circumstances today. Roman numerals are constructed 
from the letters M, D, C, L, X, V and I which represent 1000, 500, 100, 50, 10, 5 and 1 respectively. The numerals are generally written 
from largest value to smallest value. When this occurs the value of the number is the sum of the values of all of its numerals. If a smaller 
value precedes a larger value then the smaller value is subtracted from the larger value that it immediately precedes, and that difference 
is added to the value of the number. Create a recursive function that converts a Roman numeral to an integer. Your function should process 
one or two characters at the beginning of the string, and then call itself recursively on all of the unprocessed characters. Use an empty 
string, which has the value 0, for the base case. In addition, write a main program that reads a Roman numeral from the user and displays 
its value. You can assume that the value entered by the user is valid. Your program does not need to do any error checking.
'''

NUMERAL_TRANSLATION_TABLE = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

translate_individual = lambda digit: NUMERAL_TRANSLATION_TABLE[digit]

def translate(unprocessed_numeral: str, value: int = 0) -> int:
    if unprocessed_numeral == '':
        return value
    elif len(unprocessed_numeral) == 1:
        return value + translate_individual(unprocessed_numeral)

    if translate_individual(unprocessed_numeral[0]) < translate_individual(unprocessed_numeral[1]):
        value += translate_individual(unprocessed_numeral[1]) - translate_individual(unprocessed_numeral[0])
        unprocessed_numeral = unprocessed_numeral[2:]
    else:
        value += translate_individual(unprocessed_numeral[0])
        unprocessed_numeral = unprocessed_numeral[1:]

    return translate(unprocessed_numeral, value)

if __name__ == '__main__':
    numeral = input('Please input numeral: ')

    print(f'Value: {translate(numeral)}')
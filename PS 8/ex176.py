# from string import digits, punctuation, whitespace

PHONETIC_ALPHABET = {
    'A': 'Alpha ',
    'B': 'Bravo ',
    'C': 'Charlie ',
    'D': 'Delta ',
    'E': 'Echo ',
    'F': 'Foxtrot ',
    'G': 'Golf ',
    'H': 'Hotel ',
    'I': 'India ',
    'J': 'Juliet ',
    'K': 'Kilo ',
    'L': 'Lima ',
    'M': 'Mike ',
    'N': 'November ',
    'O': 'Oscar ',
    'P': 'Papa ',
    'Q': 'Quebec ',
    'R': 'Romeo ',
    'S': 'Sierra ',
    'T': 'Tango ',
    'U': 'Uniform ',
    'V': 'Victor ',
    'X': 'Xray ',
    'Y': 'Yankee ',
    'Z': 'Zulu '
}

TRASH_CHAR_COLLECTER = {48: '', 49: '', 50: '', 51: '', 52: '', 53: '', 54: '', 55: '', 56: '', 57: '', 33: '', 34: '', 35: '', 36: '', 37: '', 38: '', 39: '', 40: '', 41: '', 42: '', 43: '', 44: '', 45: '', 46: '', 47: '', 58: '', 59: '', 60: '', 61: '', 62: '', 63: '', 64: '', 91: '', 92: '', 93: '', 94: '', 95: '', 96: '', 123: '', 124: '', 125: '', 126: '', 32: '', 9: '', 10: '', 13: '', 11: '', 12: ''}
# TRASH_CHAR_COLLECTER = {ord(char):'' for char in digits+punctuation+whitespace}

def preprocess_txt(s: str) -> str:
    s = s.upper()
    s = s.translate(TRASH_CHAR_COLLECTER)
    return s[::-1] #PLEASE DON'T BE A LOOP!!!!!!!

def map_txt(reversed_ps: str, outstr='') -> str:
    if reversed_ps == '':
        return outstr
    outstr += PHONETIC_ALPHABET[reversed_ps[-1]]
    reversed_ps = reversed_ps[:-1] #PLEASE DON'T BE A LOOP!!!!!!!
    return map_txt(reversed_ps, outstr)

if __name__ == '__main__':
    txt = input('Please input a string to convert into NATO phonetic spelling: ')
    print(f'Phonetic spelling: {map_txt(preprocess_txt(txt))}')
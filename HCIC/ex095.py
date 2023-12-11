from string import ascii_letters
from ex117 import tokenise

# WORDS = list()
# with open('/Volumes/Data stuffs/Python/LCCL_Python2/PS 7/files/words.txt', 'r') as f:
#     for word in f.readlines():
#         WORDS.append(word[:-1])

# print('Note: This program operates under the assumption that all quotations are double quotation marks!')

def tokenise_(str_):
    token_filtered_1 = str_.strip().split(' ')
    token_filtered_2 = list()
    for token in token_filtered_1:
        mainword = ''
        for char in token:
            if char in ascii_letters + '-':
                mainword += char.lower()
            else:
                if mainword != '': token_filtered_2.append(mainword)
                token_filtered_2.append(char)
                mainword = ''
        if mainword != '': token_filtered_2.append(mainword)
        token_filtered_2.append(' ')
    return token_filtered_2

def capitalise(_in):
    tokens = tokenise_(_in)
    # tokens = [token.lower() for token in tokenise(_in)]
    outstr = str()
    memory = list()
    for i, token in enumerate(tokens):
        if memory == list():
            if token.isalpha():
                outstr += token.capitalize()
                memory.append(token)
            else:
                outstr += token
                memory.append(token)
        elif memory[-1] in '.!?"' or (memory[-1] == ' ' and memory[-2] in '.!?"'):
            outstr += token.capitalize()
            memory.append(token)
        elif token in ['i', 'I']:
            outstr += token.upper()
            memory.append(token)
        else:
            outstr += token
            memory.append(token)
    return outstr

if __name__ == '__main__':
    i = input("Please input a sentence: ")
    print(f'Corrected sentence: {capitalise(i)}')
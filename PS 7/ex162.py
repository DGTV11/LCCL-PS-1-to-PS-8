'''
The novel “Gadsby” is over 50,000 words in length. While 50,000 words is not normally remarkable for a novel, it is in this case because 
none of the words in the book use the letter E. This is particularly noteworthy when one considers that E is
the most common letter in English.

Write a program that reads a list of words from a file and determines what propor-
tion of the words use each letter of the alphabet. Display this result for all 26 letters and include an additional message that identifies 
the letter that is used in the smallest proportion of the words. Your program should ignore any punctuation marks that are present in the 
file and it should treat uppercase and lowercase letters as equivalent.
'''

from string import ascii_lowercase

fp = input('Please input text file path: ').strip()
if fp.endswith('\'') or fp.endswith('"'): fp = fp[:-1]
if fp.startswith('\'') or fp.startswith('"'): fp = fp[1:]

with open(fp, 'r') as f: fl = f.readlines()

class LetterProportionsInOneWord:
    def __init__(self, wordtxt):
        self.ltr_used = {char:False for char in ascii_lowercase}
        for char in wordtxt: 
            self.ltr_used[char.lower()] = char in ascii_lowercase

        self.is_useless = all(map(lambda value: value==False, self.ltr_used.values()))

LPs = []

for line in fl:
    if line.endswith('\n'): line = line[:-1]
    for word in line.split():
        LPs.append(LetterProportionsInOneWord(word))

ltr_props = {char:False for char in ascii_lowercase}

for word_obj in LPs:
    for ltr in ascii_lowercase: 
        ltr_props[ltr] += int(word_obj.ltr_used[ltr])

for ltr in ltr_props:
    print(f'Proportion of letter {ltr}: {ltr_props[ltr]/len(list(filter(lambda x: not x.is_useless, LPs))) * 100}%')

lps = sorted(ltr_props.items(), key=lambda ltr_prop: ltr_prop[1])

least_prop = lps[0][1]/len(list(filter(lambda x: not x.is_useless, LPs))) * 100
print(f'Proportion of letter with least proportion ({lps[0][0]}): {least_prop}%')
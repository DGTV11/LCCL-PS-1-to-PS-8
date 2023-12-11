import helpers as h
from string import ascii_letters
import sys

PHRASE_SEPS = ['.', ',', '?', '!', ':', ';', '"', '\'', '(', ')', '[', ']', '{', '}']   

class Checker:
    def __init__(self, file):
        self.file = file
    def phrasify(self):
        file_lines = h.read_file_lines(self.file)
        tokens = []
        phrases = []

        for ln, line in enumerate(file_lines, start=1):
            filtered_line = ''
            for char in line:
                if char in ascii_letters+' ':
                    filtered_line += char
                elif char in PHRASE_SEPS:
                    filtered_line += f' {char} '

            rawtoks = filtered_line.split()
            tokens.extend([(rawtok.lower(), rawtok, ln) for rawtok in rawtoks])

        phrase = []
        for tok in tokens:
            if tok[1] not in PHRASE_SEPS:
                phrase.append(tok)
            else:
                phrases.append(phrase)
                phrase = []
        if len(phrase) != 0:
            phrases.append(phrase)

        return phrases

    def check(self, phrases):
        bad_tokens = []

        for phrase in phrases:
            memory = None
            for token in phrase:
                if memory and token[0] == memory[0]:
                    bad_tokens.append(token)
                memory = token

        return bad_tokens

    def __str__(self):
        out_str = 'Repeated words:\n'
        for bt in self.check(self.phrasify()):
            out_str += f'{bt[1]} at line {bt[2]}\n'

        return out_str
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 "/Volumes/Data stuffs/Python/LCCL_Python2/PS 7/ex168.py" <file>')
        quit()

    fn = sys.argv[1]
    print(Checker(h.purify_fn(fn)))
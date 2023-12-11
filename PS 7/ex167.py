import helpers as h
from string import ascii_letters
import sys, os

WORDS_SET = h.read_file_lines(os.path.join(os.path.dirname(__file__), 'files/words.txt'), setify=True)

class Checker:
    def __init__(self, file):
        self.file = file
    def tokenise(self):
        file_lines = h.read_file_lines(self.file)
        tokens = []

        for ln, line in enumerate(file_lines, start=1):
            filtered_line = ''
            for char in line:
                if char in ascii_letters+' ':
                    filtered_line += char

            rawtoks = filtered_line.split()
            tokens.extend([(rawtok.lower(), rawtok, ln) for rawtok in rawtoks])

        return tokens

    def check(self, tokens):
        bad_tokens = []

        for token in tokens:
            if token[0] not in WORDS_SET:
                bad_tokens.append(token)

        return bad_tokens

    def __str__(self):
        out_str = 'Mispelled words:\n'
        for bt in self.check(self.tokenise()):
            out_str += f'{bt[1]} at line {bt[2]}\n'

        return out_str
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 "/Volumes/Data stuffs/Python/LCCL_Python2/PS 7/ex167.py" <file>')
        quit()

    fn = sys.argv[1]
    print(Checker(h.purify_fn(fn)))
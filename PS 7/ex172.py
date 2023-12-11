import sys
import helpers as h

def tokenise(file):
    lines = h.read_opened_file_lines(file, stripped=True)
    tokens = []

    for line in lines:
        for token in line.split():
            tokens.append(token)

    return tokens

def word_order_gen(order):
    for word in order:
        yield word

def filter_tokens(tokens):
    VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
    filtered_tokens = []
    for token in tokens:
        vowel_order = word_order_gen(VOWELS)
        for char in token:
            if char in VOWELS:
                '''
                try:
                    if char == next(vowel_order):
                        continue
                    break
                except StopIteration:
                    break
                '''
                if char == next(vowel_order, None): # None if gen is exhausted
                    continue
                break

        else:
            if not next(vowel_order, None): # None if gen is exhausted
                filtered_tokens.append(token)
        del vowel_order

    return filtered_tokens

if __name__ == '__main__':
    with open(h.purify_fn(sys.argv[1])) as f:
        tokens = tokenise(f)

    print(filter_tokens(tokens))
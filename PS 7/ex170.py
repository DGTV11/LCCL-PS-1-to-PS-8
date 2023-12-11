import tokenize, sys, helpers, warnings

#MMMMMMMMM
if __name__ == '__main__':
    FN = helpers.purify_fn(sys.argv[1])
    readline = lambda: open(FN, 'rb').__next__
    tokens = tokenize.tokenize(readline())

    '''
    for token in tokens:
        print(token)
    '''

    comments = []
    tok_mem: tokenize.TokenInfo|None = None
    for token in tokens:
        if token.type == tokenize.COMMENT:
            tok_mem = token
        elif token.type == tokenize.NAME and token.string == 'def':
            if token.end[0] == tok_mem.end[0] + 1:
                continue
            warnings.warn(f"No comment detected before 'def' at line {token.start[0]}", UserWarning)

    # Print the comments
    for comment in comments:
        print(comment)
'''
      4       4       4       4         4
3 + ----- - ----- + ----- - ------ + -------- ...
    2*3*4   4*5*6   6*7*8   8*9*10   10*11*12

= pi

10000th approximation:
3.141592653589538
- -----------

Underlined - I remember those digits
'''
pi = 3
prevend = 2

for i in range(15):
    ix = i+1

    term_denom = prevend*(prevend+1)*(prevend+2)
    term = 4/term_denom
    prevend += 2

    if ix % 2 != 0:
        pi += term
    else:
        pi -= term
    
    print(f'Approximation {ix}: {pi}')
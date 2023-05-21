try:
    n = int(input('Please enter a number of sides between 3 and 10: '))
    nx = n - 3
    SHAPES = ('triangle', 'square', 'pentagon', 'hexagon', 'heptagon', 'octagon', 'nonagon', 'decagon')

    if nx > len(SHAPES):
        raise ValueError
    if nx < 0:
        raise ZeroDivisionError

    print(f'A shape with {n} sides is a {SHAPES[nx]}')
except Exception:
    print('haha this is what happens if you don\'t read the instructions')
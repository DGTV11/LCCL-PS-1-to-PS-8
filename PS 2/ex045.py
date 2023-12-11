norm_lengths = ['a', 'c', 'e', 'g']
inv_lengths = ['b', 'd', 'f', 'h']

height_valid_black = [1, 3, 5, 7]
height_valid_white = [2, 4, 6, 8]

l, h = input('Input a position in a chess board like this: (a-h)(1-8): ')
h = int(h)

if (h in height_valid_black and l in norm_lengths) or (h in height_valid_white and l in inv_lengths):
    print('The tile is black')
elif (h in height_valid_white and l in norm_lengths) or (h in height_valid_black and l in inv_lengths):
    print('The tile is white')
else:
    raise TypeError('haha this is what happens if you don\'t read the instructions')
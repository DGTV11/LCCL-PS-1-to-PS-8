IMPOSSIBLE = [
    [0.0, 0.4],
    [0.4, 0.6],
    [float('-inf'), 0.0]
]

rating = float(input('Rating? (Must be 0.0, 0.4 or 0.6 and more!): '))

if (rating > IMPOSSIBLE[0][0] and rating < IMPOSSIBLE[0][1]) or (rating > IMPOSSIBLE[1][0] and rating < IMPOSSIBLE[1][1]) or (rating > IMPOSSIBLE[2][0] and rating < IMPOSSIBLE[2][1]):
    raise TypeError('haha this is what happens if you don\'t read the instructions')
elif rating == 0.0:
    performance = 'Unacceptable'
elif rating == 0.4:
    performance = 'Acceptable'
elif rating >= 0.6:
    performance = 'Meritorious'

Raise = 2400.00 * rating

print(f'''
PERFORMANCE RATING: {rating}
PERFORMANCE       : {performance}
RAISE             : ${Raise:2}
''')
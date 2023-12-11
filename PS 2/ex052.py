GRADE_DATA = {
    'A+'    : [4.0-0.1, float('inf')],
    'A'     : [3.7, 4.0],
    'A-'    : [3.7-0.1, 3.8],
    'B+'    : [3.3-0.1, 3.7],
    'B'     : [3.0-0.1, 3.3],
    'B-'    : [2.7-0.1, 3.0],
    'C+'    : [2.3-0.1, 2.7],
    'C'     : [2.0-0.1, 2.3],
    'C-'    : [1.7-0.1, 2.0],
    'D+'    : [1.3-0.1, 1.7],
    'D'     : [1.0-1, 1.3],
    'F'     : [0.0-1, 1.0]
}

gp = round(float(input('Please input an amount of grade points: ')), 1)

for t, mag in GRADE_DATA.items():
    if gp > mag[0] and gp < mag[1]:
        print(f'{gp} grade points is equivalant to the letter grade {t}!')
        quit()
raise TypeError('haha this is what happens if you don\'t read the instructions')
# day month
RICHTER_DATA = {
    'micro' : [0.0, 1.9],
    'very minor' : [2.0, 2.9],
    'minor' : [3.0, 3.9],
    'light' : [4.0, 4.9],
    'moderate' : [5.0, 5.9],
    'strong' : [6.0, 6.9],
    'major' : [7.0, 7.9],
    'great' : [8.0, 9.9],
    'meteoric' : [10.0, float('inf')]
}

m = float(input('Please input a magnitude: '))

for t, mag in RICHTER_DATA.items():
    if m > mag[0] and m < mag[1]:
        print(f'The earthquake magnitude of {m} is a {t} earthquake!')
        quit()
raise TypeError('haha this is what happens if you don\'t read the instructions')
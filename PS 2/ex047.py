# day month
SEAS_DATA = {
    'Capricorn (End of year)' : [[22, 12], [31, 12]],
    'Capricorn (Start of year)' : [[1, 1], [19, 1]],
    'Aquarius' : [[20, 1], [18, 2]],
    'Pisces' : [[19, 2], [20, 3]],
    'Aries' : [[21, 3], [19, 4]],
    'Taurus' : [[20, 4], [20, 5]],
    'Gemini' : [[21, 5], [20, 6]],
    'Cancer' : [[21, 6], [22, 7]],
    'Leo' : [[23, 7], [22, 8]],
    'Virgo' : [[23, 8], [22, 9]],
    'Libra' : [[23, 9], [22, 10]],
    'Scorpio' : [[23, 10], [21, 11]],
    'Sagittarius': [[22, 11], [21, 12]], # Isn't Sagittarius supposed to be a star???
}

d, m = input('Please input your birthday in this format: (day) (month): ').split()
d = int(d)
m = int(m)

for s,dm in SEAS_DATA.items():
    if (m > dm[0][1] and m < dm[1][1]) or (m == dm[0][1] and d >= dm[0][0]) or (m == dm[1][1] and d <= dm[1][0]):
        print(f'As your birthday falls on {d}/{m}, your zodiac is {s}')
        quit()
raise TypeError('haha this is what happens if you don\'t read the instructions')
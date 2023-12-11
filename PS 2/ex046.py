# day month
SEAS_DATA = {
    'Spring'                        : [[20, 3] ,  [20, 6]],
    'Summer'                        : [[21, 6] ,  [21, 8]],
    'Fall'                          : [[22, 8] , [20, 12]],
    'Winter (Year end)'             : [[21, 12], [31, 12]],
    'Winter (Beginning of year)'    : [[1, 1]  ,  [19, 3]]
}

d, m = input('Please input a date in this format: (day) (month): ').split()
d = int(d)
m = int(m)

for s,dm in SEAS_DATA.items():
    if (m > dm[0][1] and m < dm[1][1]) or (m == dm[0][1] and d >= dm[0][0]) or (m == dm[1][1] and d <= dm[1][0]):
        print(f'The day {d}/{m} is in the {s} season!')
        quit()
raise TypeError('haha this is what happens if you don\'t read the instructions')
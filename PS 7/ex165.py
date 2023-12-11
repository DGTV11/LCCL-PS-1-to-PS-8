'''
Write a program that uses the baby names data set described in Exercise 163 to determine which names were used 
most often within a time period. Have the user supply the first and last years of the range to analyze. Display 
the boy’s name and the girl’s name given to the most children during the indicated years.
'''

yr_range = range(1900, 2013)
yr_2_boys_girls = {year:list() for year in yr_range}

import os
BABYNAMESPATH = os.path.join(os.path.dirname(__file__), 'files/BabyNames')

for year in yr_range:
    with open(os.path.join(BABYNAMESPATH, f'{year}_BoysNames.txt'), 'r') as b, open(os.path.join(BABYNAMESPATH, f'{year}_GirlsNames.txt'), 'r') as g:
        bn_dict = {bn.split()[0]: int(bn.split()[1]) for bn in b.readlines()}
        gn_dict = {gn.split()[0]: int(gn.split()[1]) for gn in g.readlines()}
        yr_2_boys_girls[year].extend([bn_dict, gn_dict])

if __name__ == '__main__':
    start = int(input('Plz input start year: '))
    if start not in yr_2_boys_girls:
        print('Start year not in data range!')
        quit()

    end = int(input('Plz input end year: '))
    if end not in yr_2_boys_girls:
        print('End year not in data range!')
        quit()

    boy_names2counts = {}
    girl_names2counts = {}
    for boys, girls in map(lambda year: yr_2_boys_girls[year], range(start, end+1)):
        for boy_name, count in boys.items():
            boy_names2counts[boy_name] = boy_names2counts.get(boy_name, 0) + count

        for girl_name, count in girls.items():
            girl_names2counts[girl_name] = girl_names2counts.get(girl_name, 0) + count

    boy_names2counts_sorted = sorted(boy_names2counts.items(), key=lambda item: item[1], reverse=True)
    girl_names2counts_sorted = sorted(girl_names2counts.items(), key=lambda item: item[1], reverse=True)

    print(f"MOST COMMON BOY NAME IN YEAR RANGE: {boy_names2counts_sorted[0][0]}")
    print(f"MOST COMMON GIRL NAME IN YEAR RANGE: {girl_names2counts_sorted[0][0]}")
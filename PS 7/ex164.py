'''
Some names, like Ben, Jonathan and Andrew are normally only used for boys while names like Rebecca and Flora are normally only used for 
girls. Other names, like Chris and Alex, may be used for both boys and girls.

Write a program that determines and displays all of the baby names that were used for both boys and girls in a year specified by the user. 
Your program should generate an appropriate message if there were no gender neutral names in the selected year. Display an appropriate error 
message if you do not have data for the year requested by the user. Additional details about the baby names data set are included in 
Exercise 163.
'''

yr_range = range(1900, 2013)
yr_2_boys_girls = {year:set() for year in yr_range}

import os
BABYNAMESPATH = os.path.join(os.path.dirname(__file__), 'files/BabyNames')

for year in yr_range:
    with open(os.path.join(BABYNAMESPATH, f'{year}_BoysNames.txt'), 'r') as b, open(os.path.join(BABYNAMESPATH, f'{year}_GirlsNames.txt'), 'r') as g:
        bn_set = {bn.split()[0] for bn in b.readlines()}
        gn_set = {gn.split()[0] for gn in g.readlines()}
        yr_2_boys_girls[year].update(bn_set.intersection(gn_set))

if __name__ == '__main__':
    year = int(input('Plz input year: '))
    if year not in yr_2_boys_girls:
        print('No data in selected year!')
        quit()
    
    names_in_yr = yr_2_boys_girls[year]

    if not names_in_yr:
        print('No gender-neutral names in selected year!')
        quit()

    print(f'Gender-neutral names: {names_in_yr}')

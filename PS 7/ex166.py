import os
BABYNAMESPATH = os.path.join(os.path.dirname(__file__), 'files/BabyNames')

yr_range = range(1900, 2013)
distinct_boys = set()
distinct_girls = set()

for year in yr_range:
    with open(os.path.join(BABYNAMESPATH, f'{year}_BoysNames.txt'), 'r') as b, open(os.path.join(BABYNAMESPATH, f'{year}_GirlsNames.txt'), 'r') as g:
        for bn in b.readlines():
            distinct_boys.add(bn.split()[0]) 
        for gn in g.readlines():
            distinct_girls.add(gn.split()[0])

print(f'Distinct boy names: {list(distinct_boys)}')
print(f'Distinct girl names: {list(distinct_girls)}')
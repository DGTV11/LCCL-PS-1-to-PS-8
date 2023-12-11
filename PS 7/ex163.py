import os
boyspop = set()
girlspop = set()

BABYNAMESPATH = os.path.join(os.path.dirname(__file__), 'files/BabyNames')

for year in range(1900, 2013):
    for i in range(2): # 0 -> _BoysNames, 1, _GirlsNames
        suffix = '_BoysNames.txt' if i == 0 else '_GirlsNames.txt'
        with open(os.path.join(BABYNAMESPATH, str(year) + suffix), 'r') as f:
            if i == 0: boyspop.add(f.readline().split()[0])
            else: girlspop.add(f.readline().split()[0])

print(f'Most popular boy names: {list(boyspop)}')
print(f'Most popular girl names: {list(girlspop)}')
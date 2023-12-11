from helpers import InputError

protons_others = {}
symbol_protons = {}
name_protons   = {}

with open('/Volumes/Data stuffs/Python/LCCL_Python2/PS 7/files/elements.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    data = line[:-1].split(',')
    protons_others[data[0]] = f'{data[2]} ({data[1]})'
    symbol_protons[data[1]] = data[0]
    name_protons[data[2]] = data[0]

while True:
    input_ = input('Plz input symbol, name, or no of protons: ')
    if input_ == '':
        break
    print(protons_others.get(input_, symbol_protons.get(input_, name_protons.get(input_, 'INPUT NOT FOUND IN DATABASE!'))))

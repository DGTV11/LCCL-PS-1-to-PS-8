'''
101.325kpa = 1atm
1kpa = 7.5006mmhg
1kpa = (1 × 0.14503773773020923)psi
'''
kpa = float(input('Pressure in KPA: '))
atm = kpa / 101.325
mmhg = kpa * 7.5006
psi = kpa * 0.14503773773020923

print(f'''
{kpa} KPA
=
{atm} atm
=
{mmhg} mmhg
=
{psi} PSI
''')
'''
Base (50min air, 50 texts, 2GB) - $30
Extra air - $0.25/min
Extra texts - $0.15/text
Extra MiB - $5/MiB
Subtotal's 7% sales tax - 7/100 * SUBTOTAL
'''

BASE_PRICE = 30
air_time = int(input('Call time in miniutes: '))
texts = int(input('Text messages: '))
data_in_mib = int(input('Data in MiB: '))
allvars = list()
allvars.append(BASE_PRICE)

print(f'{"MONTHLY PHONE BILL":-^36s}')
print(f'{"Base price":25s}${BASE_PRICE:.>10.2f}')
if air_time > 50:
    print(f'{"Extra Air Time":25s}${((air_time - 50) * 0.25):.>10.2f}')
    allvars.append((air_time - 50) * 0.25)

if texts > 50:
    print(f'{"Extra Text Messages":25s}${((texts - 50) * 0.15):.>10.2f}')
    allvars.append((texts - 50) * 0.15)

if data_in_mib > 2048:
    print(f'{"Extra Mobile Data":25s}${((data_in_mib - 2048) * 5):.>10.2f}')
    allvars.append((data_in_mib - 2048) * 5)

subtotal = sum(allvars)

print(f'{"7% Sales Tax":25s}${(7/100 * subtotal):.>10.2f}')
print(f'{"TOTAL":25s}${((7/100 * subtotal)+subtotal):.>10.2f}')
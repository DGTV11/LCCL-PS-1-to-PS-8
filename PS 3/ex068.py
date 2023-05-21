'''
Input - ONLY 8 '1s' OR '0s' AT A TIME!

Parity - Count No. of '1s' in total (Byte + parity)
'''

while True:
    byte = input('Input 8 bits: (blank to quit):')
    if len(byte) > 8 or len(byte) - (list(byte).count('1') + list(byte).count('0')) != 0:
        raise ValueError('Invalid byte!')
    elif byte == '':
        break
    
    if list(byte).count('1') % 2 != 0:
        parity = 1
    else:
        parity = 0

    print(f'Parity bit: {parity}')
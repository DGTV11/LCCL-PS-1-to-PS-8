num = int(input("Input any 4 digit number: "))
if num > 9999 or num < 1000:
    raise ValueError('Number not 4 digits!')
digits = list(f'{num:4d}')
dig_sum = 0
for i in range(len(digits)):
    digits[i] = int(digits[i]) 
    dig_sum += digits[i]
print(f'''
- Digits of {num}: {digits}
- Digital root of {num}: {dig_sum}
''')
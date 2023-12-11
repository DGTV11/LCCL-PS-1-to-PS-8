char2province = {
    'A': 'Newfoundland',
    'B': 'Nova Scotia',
    'C': 'Prince Edward Island',
    'E': 'New Brunswick',
    'G': 'Quebec',
    'H': 'Quebec',
    'J': 'Quebec',
    'K': 'Ontario',
    'L': 'Ontario',
    'M': 'Ontario',
    'N': 'Ontario',
    'P': 'Ontario',
    'R': 'Manitoba',
    'S': 'Saskatchewan',
    'T': 'Alberta',
    'V': 'British Columbia',
    'X': 'Nunavut/Northwest Territories',
    'Y': 'Yukon'
}

x = input('Input postal code: ').replace(' ', '')
if x[0].isupper() and x[2].isupper() and x[4].isupper() and x[1].isnumeric() and x[3].isnumeric() and x[5].isnumeric:
    print(f'Approx. location: {char2province[x[0]]} ({"rural" if x[1] == "0" else "urban"})')
else:
    print('Invalid postal code!')
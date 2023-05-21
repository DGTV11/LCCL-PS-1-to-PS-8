let = input('Input ONE letter: ')
VOWS = ('a', 'e', 'i', 'o', 'u')

if len(let) > 1:
    raise ValueError('haha this is what happens if you don\'t read the instructions')
elif not let.isalpha():
    raise ValueError('haha this is what happens if you don\'t read the instructions')
elif let.lower() in VOWS:
    print(f'{let} is definitely a vowel!')
elif let.lower() == 'y':
    print(f'Sometimes {let} is a vowel, and sometimes {let} is a consonant!')
else:
    print(f'{let} is definitely a consonent!')
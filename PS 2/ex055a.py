m = float(input('Please input a frequency in Hz: '))

if m < 0:
    raise TypeError('OUTSIDE OF VALID SPECTRUM!')
elif m < 3e9:
    t = 'Radio waves'
elif m < 3e12:
    t = 'Microwaves'
elif m < 4.3e14:
    t = 'Infared light'
elif m < 7.5e14:
    t = 'Visible light'
elif m < 3e17:
    t = 'Ultraviolet light'
elif m < 3e19:
    t = 'X-rays'
else:
    t = 'Gamma rays'

print(f'''
If you were using some cell tower hidden in your basement blasting out 
energy with the frequency of {m}Hz, you will be sending out {t} to intefere with 
your neighbourhood! XD (not liable for anything related to that cell tower hidden 
in your basement)
''')
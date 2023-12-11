RICHTER_DATA = {
    'Radio waves' : [0, 3e9],
    'Microwaves' : [3e9, 3e12],
    'Infared light' : [3e12, 4.3e14],
    'Visible light' : [4.3e14, 7.5e14],
    'Ultraviolet light' : [7.5e14, 3e17],
    'X-rays' : [3e17, 3e19],
    'Gamma rays' : [3e19, float('inf')]
}

m = float(input('Please input a frequency in Hz: '))

for t, mag in RICHTER_DATA.items():
    if m >= mag[0] and m < mag[1]:
        print(f'''If you were using some cell tower hidden in your basement blasting out 
    energy with the frequency of {m}Hz, you will be sending out {t} to intefere with 
    your neighbourhood! XD (not liable for anything related to that cell tower hidden 
    in your basement)''')
        quit()
raise TypeError('OUTSIDE OF VALID SPECTRUM!')
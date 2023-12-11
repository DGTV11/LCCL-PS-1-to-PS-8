m = float(input('Please input a wavelength in the visible light spectrum in nm: '))

if m < 380:
    raise TypeError('OUTSIDE OF VISIBLE SPECTRUM!')
elif m < 450:
    t = 'Violet'
elif m < 495:
    t = 'Blue'
elif m < 570:
    t = 'Green'
elif m < 590:
    t = 'Yellow'
elif m < 620:
    t = 'Orange'
elif m <= 750:
    t = 'Red'
else:
    raise TypeError('OUTSIDE OF VISIBLE SPECTRUM!')

print(f'{m}nm => {t}')
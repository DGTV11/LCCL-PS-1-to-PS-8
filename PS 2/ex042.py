NOTE_DATA = {
    261.63      : 'C4',      
    293.66      : 'D4',      
    329.63      : 'E4',      
    349.23      : 'F4',
    392.00      : 'G4', 
    440.00      : 'A4',
    493.88      : 'B4',
}

freq = float(input('Please input a note in octave 4 in Hz: '))
for f,n in NOTE_DATA.items():
    if freq > f-1 and freq < f+1:
        print(f'The frequency {freq}Hz is close to the note {n}!')
        quit()
raise TypeError('haha this is what happens if you don\'t read the instructions')
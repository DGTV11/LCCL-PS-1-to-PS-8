try:

    NOTE_DATA = {
        'C'     : 261.63,
        'D'     : 293.66,
        'E'     : 329.63,
        'F'     : 349.23,
        'G'     : 392.00,
        'A'     : 440.00,
        'B'     : 493.88,
    }

    scalept = input('Please input a note THAT EXISTS: ')
    # print(f'DEBUG: {list(scalept)}')
    note = scalept[0]
    octave = int(scalept[1])

    '''
    2^4−x

    x = octave
    '''

    if note.upper() in NOTE_DATA:
        print(f'The note {scalept.upper()} has the frequency of {NOTE_DATA[note.upper()]/(2**(4-octave))}Hz!')
    else:
        raise TypeError
except:
    print('haha this is what happens if you don\'t read the instructions')
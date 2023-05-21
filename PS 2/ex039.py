jackhammer = 130
lawnmower = 106
alarm_clock = 70
quiet_room = 40

dB = int(input('Sound level in decibels: '))

if dB > jackhammer:
    print('The noise is louder than an average jackhammer!')

elif dB == jackhammer:
    print('The noise is as loud as an average jackhammer!')

elif dB < jackhammer and dB > lawnmower: #lawnmower < dB < jackhammer
    print('The noise is between an average jackhammer and an average lawnmower!')

elif dB == lawnmower:
    print('The noise is as loud as an average lawnmower!')

elif dB < lawnmower and dB > alarm_clock:
    print('The noise is between an average lawnmower and an average alarm clock!')

elif dB == alarm_clock:
    print('The noise is as loud as an average alarm clock!')

elif dB < alarm_clock and dB > quiet_room:
    print('The noise is between an average alarm clock and an average quiet room!')

elif dB == quiet_room:
    print('The noise is as loud as an average quiet room!')

elif dB < quiet_room:
    print('The noise is quieter than an average quiet room!')
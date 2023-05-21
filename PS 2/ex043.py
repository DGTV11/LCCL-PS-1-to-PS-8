NOTE_DATA = {
    1   : 'George Washington',
    2   : 'Thomas Jefferson',
    5   : 'Abraham Lincoln',
    10  : 'Alexander Hamilton',
    20  : 'Andrew Jackson',
    50  : 'Ulysses S. Grant',
    100 : 'Benjamin Franklin',
}

note = int(input('Please input a US note that EXISTS: $'))
if note in NOTE_DATA:
    print(f'The US note ${note} has the face of {NOTE_DATA[note]} printed on the note!')
else:
    raise TypeError('haha this is what happens if you don\'t read the instructions')
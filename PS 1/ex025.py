# DEFINE CONSTANTS
MIN = 60
HOUR = MIN*60
DAY = HOUR*24

# BEGIN PROGRAM
initsecs = int(input('Seconds (Whole numbers only): '))
secs = initsecs

## Days
days = secs // DAY
secs %= DAY

## Hours
hours = secs // HOUR
secs %= HOUR

## Minutes
mins = secs // MIN
secs %= MIN

print(f'{initsecs} seconds = {days}:{hours:02d}:{mins:02d}:{secs:02d}')
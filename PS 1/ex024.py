# Constants
SECOND = 1
MIN = 60
HOUR = MIN*60
DAY = HOUR*24

# Main
seconds = int(input('Seconds (Whole numbers only): '))
minutes = int(input('Minutes (Whole numbers only): '))
hours = int(input('Hours (Whole numbers only): '))
days = int(input('Days (Whole numbers only): '))

final = seconds + (minutes*MIN) + (hours*HOUR) + (days*DAY)

print(f'''
{seconds} seconds
+
{minutes} minutes
+
{hours} hours
+
{days} days
=
{final} seconds
''')
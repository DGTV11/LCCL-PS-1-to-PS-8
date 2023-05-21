'''
In the United States, fuel efficiency for vehicles is normally expressed in miles-per- gallon (MPG).
In Canada, fuel efficiency is normally expressed in liters-per-hundred kilometers (L/100 km).
Use your research skills to determine how to convert from MPG to L/100 km.
Then create a program that reads a value from the user in American units and displays the equivalent
fuel efficiency in Canadian units.
'''


def fuelConversion(fuel): #https://www.reddit.com/r/learnpython/comments/g7dtq1/mpg_to_l100km_and_viceversa/
    g = 3.785411784   # liters per gallon
    m = 1609.344    # meters per mile
    kpg = (g / m * 1000)    # kilometers per gallon
    return 100 / fuel * kpg    # returns fuel as mpg to l/100km or vice versa

print('Canadian efficiency: %f'%fuelConversion(float(input('MPG: '))))
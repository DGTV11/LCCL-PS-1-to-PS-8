WIDGET_WEIGHT = 75
GIZMO_WEIGHT = 112

x = input('''
Please input the amount of widgets and gizmos you would like to buy in this order; WWW GGG, below (Any floating point numbers will be rounded down)
VVV
''')

wg = x.split()
total_weight = (int(wg[0])*WIDGET_WEIGHT) + (int(wg[1]) * GIZMO_WEIGHT)

print('Total weight: %ig'%total_weight)
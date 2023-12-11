r_1l_or_less = int(input('Amount of drink containers holding one liter or less (INTEGERS ONLY!): '))*0.10
r_more_than_1l = int(input('Amount of drink containers holding more than one liter(INTEGERS ONLY!): '))*0.25
print('Possible refund (Any floating point numbers were rounded down): $%s'%(float(r_1l_or_less)+float(r_more_than_1l)))

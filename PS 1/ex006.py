icom = float(input('Intital cost of meal: $'))
TAXRATE = 0.10
tax = icom*TAXRATE
tip = icom*0.18
total = icom+tax+tip

print('RESTAURANT BILL:')
#ICOM
if icom >= 10:
    print('COST: $%s'%str(icom))
else:
    print('COST: $0%s'%str(icom))

#TAX
if tax >= 10:
    print('TAX: $%s'%str(tax))
else:
    print('TAX: $0%s'%str(tax))

#TIP
if tip >= 10:
    print('TIP: $%s'%str(tip))
else:
    print('TIP: $0%s'%str(tip))

#TOTAL
if total >= 10:
    print('TOTAL: $%s'%str(total))
else:
    print('TOTAL: $0%s'%str(total))
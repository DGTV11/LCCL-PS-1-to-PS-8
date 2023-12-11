p = float(input('Amount of money deposited: $'))
r = 0.04

for t in range(1, 4):
    output = p*((1+r)**t)
    print(f"{str(t)} years: ${output:.2f}")
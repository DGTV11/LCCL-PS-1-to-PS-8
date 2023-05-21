def med(vals):
    v = vals
    highest = v[0]
    for item in v:
        if item > highest:
            highest = item
    
    v.remove(highest)
    return max(v[0], v[1])


if __name__ == "__main__":
    v = list()
    for i in range(3):
        v.append(float(input('Please input a value: ')))
    
    print(f'The median of the three inputed values is {med(v)}.')
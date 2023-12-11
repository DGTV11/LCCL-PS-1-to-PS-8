import helpers
def py2ELlist(l):
    if len(l) == 0:
        raise helpers.InputError('Invalid list length (0 inputed, 1 or more expected)')
    elif len(l) == 1:
        return str(l[0])
    elif len(l) == 2:
        return f'{l[0]} and {l[1]}'
    else:
        x = str()
        for item in l[:-1]:
            x += f'{item}, '
        x += f'and {l[-1]}'
        return x
    
if __name__ == '__main__':
    l = list()
    while True:
        x = input('Input item: ')
        if x.strip() == '':
            break
        l.append(x)
    
    print(f'Formatted list: {py2ELlist(l)}')
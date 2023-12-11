from os import path

ELEMENTS_FILE_PATH = path.join(path.dirname(__file__), 'files/elements.txt')

def load_elements_symbols(fp: str) -> list[str]:
    symbols = []
    
    with open(fp, 'r') as f:
        for line in f.readlines():
            symbols.append(line.split(',')[1])
            
    return symbols

def search(tgt_str: str, elements_symbols: list[str], elements_repr: list[str] = []) -> tuple[bool, list[str]]:

    if tgt_str == '':
        return (True, elements_repr)

    for symbol in elements_symbols:
        symbol_len = len(symbol)

        if len(tgt_str) < symbol_len:
            continue
        
        if tgt_str[:symbol_len].upper() == symbol.upper():
            search_res = search(tgt_str[symbol_len:], elements_symbols, elements_repr+[symbol])
            # print(search_res) #**DEBUG**
            if search_res[0]:
                return search_res

    return (False, [])

def ret_search(tgt_str: str, elements_symbols: dict) -> str:
    can_spell, elements_repr = search(tgt_str, elements_symbols)

    if can_spell:
        return f'{tgt_str} can be spelled as ' + ''.join(elements_repr)
    
    return f'{tgt_str} cannot be spelled with element symbols'

def load_elements_names(fp: str) -> list[str]:
    with open(fp, 'r') as f:
        return [line.split(',')[2].strip() for line in f.readlines()]

if __name__ == '__main__':
    elements_symbols = load_elements_symbols(ELEMENTS_FILE_PATH)

    '''
    # TEST
    tgt_str = input('Search for: ')

    print(ret_search(tgt_str, elements_symbols))
    '''

    elements_names = load_elements_names(ELEMENTS_FILE_PATH)

    for name in elements_names:
        print(ret_search(name, elements_symbols))
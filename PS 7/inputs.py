def iterInputList_OnePerLine(text='Please input number (blank to quit): ', error='ERROR: Incorrect input type!', _type=int, func=None, func_text='', quitter='', _continue=False):
    '''
    text -> input text (e.g: 'Please input number (blank to quit): ' )\n
    error -> error if cannot change type (e.g: 'ERROR: Incorrect input type!')\n
    _type -> type to change input to (can sometimes be a function)\n
    func -> function to pass transformed input to (optional)\n
    func_text -> text to output after func is run ({_func} -> output of func)\n
    quitter -> text in which this function ends when entered (usually 0 or blank)\n
    _continue -> continue if transformation throws error (True or False)\n
    '''
    _list = list()
    while True:
        x = input(text) 
        if x == quitter: #usually 0 or blank
            break
        else:
            try:
                _list.append(_type(x))
                if func:
                    y = func(_list)
                    print(func_text.format(_func=str(y)))
            except (ValueError, TypeError):
                print(error)
                if not _continue:
                    break
                else:
                    continue
    return _list

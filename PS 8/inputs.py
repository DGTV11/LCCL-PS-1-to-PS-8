def iterInputList_OnePerLine(text='Please input number (blank to quit): ', error='ERROR: Incorrect input type!', _type=int, func=None, func_text='', quitter='', _continue=False):
    '''
    text -> input text (e.g: 'Please input number (blank to quit): ' )
    error -> error if cannot change type (e.g: 'ERROR: Incorrect input type!')
    _type -> type to change input to (can sometimes be a function)
    func -> function to pass transformed input to (optional)
    func_text -> text to output after func is run ({_func} -> output of func)
    quitter -> text in which this function ends when entered (usually 0 or blank)
    _continue -> continue if transformation throws error (True or False)
    '''
    _list = list()  # Create an empty list to store the inputs
    while True:  # Continue looping until a break statement is encountered
        x = input(text)  # Prompt the user for input
        if x == quitter:  # Check if the input matches the quitter text
            break  # Exit the loop if the input matches the quitter text
        else:
            try:
                _list.append(_type(x))  # Convert the input to the specified type and append it to the list
                if func:
                    y = func(_list)  # Pass the transformed input to the specified function
                    print(func_text.format(_func=str(y)))  # Print the output of the function
            except (ValueError, TypeError):
                print(error)  # Print the error message if the input cannot be converted to the specified type
                if not _continue:
                    break  # Exit the loop if continue is set to False
                else:
                    continue  # Continue the loop if continue is set to True
    return _list  # Return the list of inputs

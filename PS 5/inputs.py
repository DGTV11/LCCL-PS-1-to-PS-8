def inpList(text, _type, quitter):
    l = list()
    while True:
        x = input(text) #"Please input an integer (all floats will be integerised, type 0 to quit): "

        if x == quitter: #0 or blank
            break
        else:
            exec(f"l.append({_type}(x))")
    return l
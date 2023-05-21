def list2english(_list):
    eng = str()
    for i, item in enumerate(_list):
        if i == len(_list) - 1 and len(_list) != 1:
            eng += f"and {item}"
        elif len(_list) == 1:
            eng = item
        elif i == len(_list) - 2:
            eng += f"{item} "
        else:
            eng += f"{item}, "
    return eng
    
if __name__ == '__main__':
    items = list()
    e = input("Please input an item (blank to stop): ")
    while e == str():
        e = input("Please input an item (blank to stop): ")
        items.append(e)
    print(f"""{items}\n==\n{list2english(items)}""")
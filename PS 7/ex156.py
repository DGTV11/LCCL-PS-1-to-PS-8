from inputs import iterInputList_OnePerLine

iterInputList_OnePerLine(text='Please input float or int number (blank to quit): ', _type=float, func=lambda l: sum(l), func_text='Current sum: {_func}', _continue=True)
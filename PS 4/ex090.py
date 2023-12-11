from ex089 import *

'''
a partridge in a pear tree
two turtle doves
three French hens
four calling birds
five gold rings
six geese a-laying
seven swans a-swimming
eight maids a-milking
nine ladies dancing
ten lords a-leaping
eleven pipers piping
twelve drummers drumming
'''

gifts = [
    "And a partridge in a pear tree.",
    "Two turtle doves,",
    "Three French hens,",
    "Four calling birds,",
    "Five gold rings,",
    "Six geese a-laying,",
    "Seven swans a-swimming,",
    "Eight maids a-milking,",
    "Nine ladies dancing,",
    "Ten lords a-leaping,",
    "Eleven pipers piping,",
    "Twelve drummers drumming,"
]

text = ""

def addtotext(txt):
    global text
    text = text + "\n" + txt

def cleartext():
    global text
    text = ""

def verse(No):
    global text
    cleartext()

    addtotext(f"On the {ordinise(No)} day of Christmas")
    addtotext("my true love sent to me:")
    if No == 1:
        addtotext("A partridge in a pear tree.")
    else:
        gifts_in_verse = list()
        for i in range(No):
            gifts_in_verse.append(gifts[i])
        gifts_in_verse.reverse()

        for item in gifts_in_verse:
            addtotext(item)

    return text

for i in range(1, 13):
    print(verse(i))

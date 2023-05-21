"""
Words like first, second and third are referred to as 
ordinal numbers. In this exercise, you will write a 
function that takes an integer as its only parameter 
and returns a string containing the appropriate 
English ordinal number as its only result. Your 
function must handle the integers between 1 and 12 
(inclusive). It should return an empty string if the 
function is called with an argument outside of this 
range. Include a main program that demonstrates your 
function by displaying each integer from 1 to 12 and 
its ordinal number. Your main program should only run 
when your file has not been imported into another program.
"""

TRANSLATIONTABLE = {
    1 : "First",
    2 : "Second",
    3 : "Third",
    4 : "Fourth",
    5 : "Fifth",
    6 : "Sixth",
    7 : "Seventh",
    8 : "Eighth",
    9 : "Ninth",
    10: "Tenth",
    11: "Eleventh",
    12: "Twelveth"
}

def ordinise(_int):
    if _int < 1 or _int > 12:
        return None
    
    return TRANSLATIONTABLE[_int]

if __name__ == "__main__":
    for i in range(1, 13):
        print(f"{str(i)} {ordinise(i)}")
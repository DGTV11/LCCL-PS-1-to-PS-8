END_PUNCTUATION = [".", "!", "?"]

def capitalisation(text):
    t = text

    ot = list()
    output = str()

    for char in t:
        if t.index(char) == 0:
            ot.append(char.upper())
        elif t.index(char) >= 2:
            if ot[-2] in END_PUNCTUATION:
                ot.append(char.upper()) 
            elif t.index(char) > 0 and char in ["i", "I"]:
                if ot[-1] == " " and (t[len(ot) + 1] in [" ", ".", "!", "?", "'", "’"]): 
                    ot.append(char.upper())
                elif char.isalpha():
                    ot.append(char.lower())
                else:
                    ot.append(char)  
            elif char.isalpha():
                ot.append(char.lower())
            else:
                ot.append(char) 
        elif t.index(char) > 0 and char in ["i", "I"]:
            if ot[-1] == " " and (t[len(ot) + 1] in [" ", ".", "!", "?", "'", "’"]):
                ot.append(char.upper())
            elif char.isalpha():
                ot.append(char.lower())
            else:
                ot.append(char)
        elif char.isalpha():
            ot.append(char.lower())
        else:
            ot.append(char)

    for char in ot:
        output += char

    return output

if __name__ == "__main__":
    ct = capitalisation(input("Text to correct:\n"))
    print(f"Corrected text:\n{ct}")
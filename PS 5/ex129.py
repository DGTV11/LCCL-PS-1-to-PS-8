BINARY = ["*", "/", "^", "-", "+"]
UNARY = ["-", "+"]
PARENTESEES = ["(", ")"]

def math_tokenise(equation_str):
    num_bin = str()
    token_list = list()

    for i, item in enumerate(equation_str+" "):
        if item == " " and i != len(equation_str): # Whitespace handler
            continue
        elif ((item in BINARY+PARENTESEES or i == len(equation_str))
                and num_bin != str()): # Number to token list forwarder
            token_list.append(num_bin)
            num_bin = str()

        if ((item in UNARY and i == 0)
                or (item in UNARY and token_list != list() and token_list[-1] in BINARY+["("])
                or item.isnumeric()): # Unary handler
            num_bin += item
        elif ((num_bin == str() and item in BINARY) 
                or item in PARENTESEES): # Binary handler
            token_list.append(item)
    
    return token_list

if __name__ == "__main__":
    print(math_tokenise(input("INPUT MATH EXPRESSION: ")))
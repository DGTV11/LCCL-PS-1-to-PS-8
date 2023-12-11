from ex129 import math_tokenise, UNARY

def identify_unary(token_list):
    new_token_list = list()

    for item in token_list:
        if item[-1].isnumeric() and item[0] in UNARY:
            new_token_list.append("u"+item[0])
            new_token_list.append(item[1:])
        else:
            new_token_list.append(item)

    return new_token_list

if __name__ == "__main__":
    print(identify_unary(math_tokenise(input("INPUT MATH EXPRESSION: "))))
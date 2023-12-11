OPS = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "u+": 3,
    "u-": 3,
    "^": 4
}

def precedence(operator):
    if not (operator in OPS.keys()):
        raise ValueError("The input is not an operator!")
    else:
        return OPS[operator]

'''
Create a new empty list, operators
Create a new empty list, postfix

For each token in the infix expression
    If the token is an integer then
        Append the token to postfix
    If the token is an operator then
        While operators is not empty and
                the last item in operators is not an open parenthesis and
                precedence(token) < precedence(last item in operators) do
            Remove the last item from operators and append it to postfix
        Append the token to operators
    If the token is an open parenthesis then
        Append the token to operators
    If the token is a close parenthesis then
        While the last item in operators is not an open parenthesis do
            Remove the last item from operators and append it to postfix
        Remove the open parenthesis from operators

While operators is not the empty list do
    Remove the last item from operators and append it to postfix

Return postfix as the result of the algorithm
'''

from ex129 import BINARY, math_tokenise
from ex130 import identify_unary

def infix_to_postfix(infix):
    operators = list()
    postfix = list()

    for token in infix:
        if token.isnumeric():
            postfix.append(token)
        elif token in BINARY + ["u+", "u-"]:
            while (operators != list()) and (operators[-1] != "(") and (precedence(token) < precedence(operators[-1])):
                postfix.append(operators[-1])
                operators.pop()
            operators.append(token)
        elif token == "(":
            operators.append(token)
        elif token == ")":
            while operators[-1] != "(":
                postfix.append(operators[-1])
                operators.pop()
            operators.pop()
        
    while operators != list():
        postfix.append(operators[-1])
        operators.pop()
    
    return postfix

if __name__ == '__main__':
    print(infix_to_postfix(identify_unary(math_tokenise(input("INPUT MATH EXPRESSION: ")))))
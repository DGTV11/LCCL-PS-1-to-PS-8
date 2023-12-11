'''
Create a new empty list, values

For each token in the postfix expression
    If the token is a number then
        Convert it to an integer and append it to values
    Else if the token is a unary minus then
        Remove an item from the end of values
        Negate the item and append the result of the negation to values
    Else if the token is a binary operator then
        Remove an item from the end of values and call it right
        Remove an item from the end of values and call it left
        Compute the result of applying the operator to left and right
        Append the result to values

Return the first item in values as the value of the expression
'''
from ex129 import MATH_OPERATORS, math_tokenise
from ex130 import identify_unary
from ex131 import infix_to_postfix

def evalPostfix(postfix):
    values = list()

    for token in postfix:
        if token.isnumeric():
            values.append(int(token))
        elif token == 'u-':
            e = values[-1]
            values.pop()
            values.append(-e)
        elif token in MATH_OPERATORS:
            l = values[-1]
            values.pop()
            r = values[-1]
            values.pop()
            values.append(eval(f"{l}{token}{r}"))
        
        return values[0]

if __name__ == '__main__':
    print(evalPostfix(infix_to_postfix(identify_unary(math_tokenise(input("INPUT MATH EXPRESSION: "))))))
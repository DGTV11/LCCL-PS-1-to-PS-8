def is_palindrome(string: str) -> bool:
    if len(string) < 2:
        return True
    
    if string[0] == string[-1] and is_palindrome(string[1:-1]):
        return True

    return False

if __name__ == '__main__':
    string = input('Please input string: ')

    print(f'{string} is a palindrome' if is_palindrome(string) else f'{string} is not a palindrome')
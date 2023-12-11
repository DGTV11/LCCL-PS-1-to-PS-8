from collections import deque

def encode_list(plain: deque, encoded: list = []): #Can use list.pop(0) JIC you can't use a deque
    if len(plain) == 0:
        return encoded
    
    first_item = plain.popleft()
    no_of_first_items = 1
    if len(plain) != 0:
        while plain[0] == first_item:
            if len(plain) == 0:
                break

            plain.popleft()
            no_of_first_items += 1

    encoded.append(first_item)
    encoded.append(no_of_first_items)

    return encode_list(plain, encoded)

if __name__ == '__main__':
    l = deque(input('Please input string to be compressed:'))
    print(f'Encoded string: {encode_list(l)}')
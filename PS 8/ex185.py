
def decode_list(encoded, decoded=[]):
    if len(encoded) == 0:
        return decoded
    
    if len(encoded) % 2 != 0:
        raise TypeError('Invalid encoded list length')
    
    if encoded[1] == 0:
        return decode_list(encoded[2:], decoded)
    
    decoded.append(encoded[0])
    encoded[1] -= 1
    return decode_list(encoded, decoded)

if __name__ == '__main__':
    print(f'''
Encoded list: ["A", 12, "B", 4, "A", 6, "B", 1]
Decoded list: {decode_list(["A", 12, "B", 4, "A", 6, "B", 1])}
''')
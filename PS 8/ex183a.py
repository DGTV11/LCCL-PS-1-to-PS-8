from os import path

ELEMENTS_FILE_PATH = path.join(path.dirname(__file__), 'files/elements.txt')
    
def load_elements_names(fp: str) -> dict[str, list[str]]:
    letter_buckets = {}
    
    with open(fp, 'r') as f:
        for line in f.readlines():
            name = line.split(',')[2].strip()
            first_letter = name[0]
            if first_letter in letter_buckets:
                letter_buckets[first_letter].append(name)
            else:
                letter_buckets[first_letter] = [name]
            
    return letter_buckets

def search(element_names: list[str], element_name_buckets: dict[str, list[str]]) -> list[str]:
    avail_bucket = element_name_buckets.get(element_names[-1][-1].upper(), None)

    if not avail_bucket: 
        return element_names

    longest_name_list: list[str] = []
    for name in avail_bucket:
        if name in element_names:
            continue
        possible_longest_name_list = search(element_names + [name], element_name_buckets)
        if len(possible_longest_name_list) > len(longest_name_list):
            longest_name_list = possible_longest_name_list

    return longest_name_list or element_names

def ret_search(start_name: str, element_name_buckets: dict[str, list[str]]) -> tuple[str|None, str|None]: # (error, output)
    for bucket_view in element_name_buckets.values():
        if start_name in bucket_view:
            break
    else:
        return f'{start_name} is an invalid element name', None

    longest_list = search([start_name], element_name_buckets)

    return None, f'The longest list that starts from {start_name} is ' + ', '.join(longest_list)

if __name__ == '__main__':
    elements_name_buckets = load_elements_names(ELEMENTS_FILE_PATH)

    start_name = input('Please enter an element name: ')

    error, output = ret_search(start_name, elements_name_buckets)
    if error:
        print(error)
    else:
        print(output)
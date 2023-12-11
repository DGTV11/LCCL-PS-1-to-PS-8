from os import path

ELEMENTS_FILE_PATH = path.join(path.dirname(__file__), 'files/elements.txt')

get_bucket_idx = lambda l: ord(l) - 97 #MUST INPUT: 1 ENGLISH letter which is LOWERCASE

def load_elements_names(fp: str) -> list[list[str]]:
    letter_buckets = [[] for _ in range(26)]
    
    with open(fp, 'r') as f:
        for line in f.readlines():
            name = line.split(',')[2].strip()
            first_letter = name[0]
            bucket_idx = get_bucket_idx(first_letter.lower())
            letter_buckets[bucket_idx].append(name)
            
    return letter_buckets

def search(element_names: list[str], element_name_buckets: list[list[str]]) -> list[str]:
    avail_bucket = element_name_buckets[get_bucket_idx(element_names[-1][-1])]

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
    first_letter_bucket = element_name_buckets[get_bucket_idx(start_name[0].lower())]
    if start_name not in first_letter_bucket:
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
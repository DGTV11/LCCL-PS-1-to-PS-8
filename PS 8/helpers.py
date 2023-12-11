import sys
import io

class InputError(BaseException): pass

def ready_import_outofdir(fileOrDir): sys.path.append(fileOrDir) #appends file path or directory path to sys.path

def read_file_lines(fn: str, stripped: bool = True, setify: bool = False) -> list[str]|set[str]:
    with open(fn, 'r') as f:
        lines: list[str] = f.readlines()
        lines_filtered: list[str] = lines if not stripped else [line.strip() for line in lines]
    return lines_filtered if not setify else set(lines_filtered)

def read_opened_file_lines(file: io.TextIOWrapper, stripped: bool=True, setify=False) -> list[str]|set[str]:
    lines: list[str] = file.readlines()
    lines_filtered: list[str] = lines if not stripped else [line.strip() for line in lines]
    return lines_filtered if not setify else set(lines_filtered)

def batch_replace(_str: str, mapper: dict[str, str]|list[str]) -> str:
    if type(mapper) is dict:
        for key, value in mapper.items():
            _str = _str.replace(key, value)
    elif type(mapper) is list:
        for item in mapper:
            _str = _str.replace(item, '')
    else:
        raise InputError('Mapper must be a dict mapping string to string or list of strings')
    return _str
    
def purify_fn(fn: str):
    #Converts file name to file name without any quotes on its side
    return batch_replace(fn, ["\"", "'"])
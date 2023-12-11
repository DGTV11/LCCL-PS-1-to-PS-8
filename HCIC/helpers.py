import sys

def cmd_args(): return sys.argv #returns sys.argv
def ready_import_outofdir(fileOrDir): sys.path.append(fileOrDir) #appends file path or directory path to sys.path
def make_file(file): 
    x = open(file, 'x') 
    x.close()
def read_file_lines(file, opened=False):
    if not opened:
        with open(file, 'r') as x:
            return x.readlines()
    else:
        return file.readlines()
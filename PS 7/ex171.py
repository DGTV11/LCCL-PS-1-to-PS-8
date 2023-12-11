import sys
import helpers as h

# TEST: /usr/local/bin/python3.10 "/Volumes/Data stuffs/Python/LCCL_Python2/PS 7/ex171.py" '/Volumes/Data stuffs/Python/LCCL_Python2/PS 7/files/alice.txt'

def file_wrap_print(fn, no_chars):

    # Convert file to string
    with open(fn, 'r') as f:
        block = f.read()

    block.replace('\n', ' ')
    words = block.split()

    # Print
    line_char_count = 0
    for word in words:
        if (x := line_char_count + len(word)) >= no_chars:
            print(word+'\n' if x == no_chars else '\n'+word+' ', end='')
            line_char_count = 0 if x == no_chars else len(word+' ')
        elif line_char_count < no_chars:
            print(word, end=' ')
            line_char_count += len(word+' ')
    print()

    '''
    #*ALTERNATIVE:
    for word in words:
    if not len(word) + currentLength > LINE_LENGTH:
        newLine.append(word)
        currentLength += len(word) + 1 #account for space
    else: 
        print(" ".join(newLine))
        newLine = []
        currentLength = 0 
    print(" ".join(newLine))
    '''

    ''' 
    #! OLD DIRECT BUFFER READ, DOES NOT WORK FOR PROPER LENGTH WORD WRAP
    buf_size = sys.getsizeof('e' * no_chars)
    
    with open(fn, 'r') as f:
        while True:
            block = f.read(buf_size)
            if block == '': break
            print(block.replace('\n', ' '))
    '''

if __name__ == '__main__':
    file_wrap_print(h.purify_fn(sys.argv[1]), 50)
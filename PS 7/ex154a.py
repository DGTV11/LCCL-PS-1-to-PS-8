import sys, string

sys.path.append('/Volumes/Data stuffs/Python/LCCL_Python2/PS 6')
from ex136 import reverseLookup

if len(sys.argv) != 2:
    raise IndexError(f'ERROR: Wrong amount of input (files) (1 file needed, {len(sys.argv)-1} given)')

count = {letter:0 for letter in string.ascii_lowercase}

letters = list()
with open(sys.argv[1], 'r') as f:
# with open('/Volumes/Data stuffs/Python/LCCL_Python2/PS 7/files/jigglypuff.txt', 'r') as f:
    for line in f:
        for char in line:
            if char in string.ascii_letters:
                letters.append(char.lower())

for letter in letters:
    count[letter] += 1

sorted_letters_freqs = sorted(count.values(), reverse=True)

print('FREQUENCIES:')
for freqs in sorted_letters_freqs:
    for letter in reverseLookup(count, freqs):
        print(f'{letter} -> {count[letter]} OCCOURENCES')
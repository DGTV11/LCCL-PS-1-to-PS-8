# python3.6 '/Volumes/Data stuffs/Python/LCCL_Python2/PS 7/ex155.py' '/Volumes/Data stuffs/Python/LCCL_Python2/PS 7/files/ex155-test.txt'

import sys, string

if len(sys.argv) != 2:
    raise IndexError(f'ERROR: Wrong amount of input (files) (1 file needed, {len(sys.argv)-1} given)')

words = list()
with open(sys.argv[1], 'r') as f:
# with open('/Volumes/Data stuffs/Python/LCCL_Python2/PS 7/files/jigglejiggle.txt', 'r') as f:
    for line in f:
        for token in line.split():
            raw_word = str()
            leading = 0
            trailing = len(token) - 1

            while not token[leading].isalpha():
                leading += 1

            while not token[trailing].isalpha():
                trailing -= 1

            words.append(token[leading:trailing+1].lower())

count = {word:0 for word in list(set(words))}
for word in words:
    count[word] += 1
    
sorted_by_freq = sorted(count.items(), key=lambda item: item[1], reverse=True)
highest_freq = sorted_by_freq[0][1]

for most_freq_word in sorted_by_freq:
    if most_freq_word[1] != highest_freq: break
    print(f'MOST FREQUENT WORD: {most_freq_word[0]} -> {most_freq_word[1]} OCCOURENCES')
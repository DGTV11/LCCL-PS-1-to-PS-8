'''
Students learning to spell in English are often taught the rhyme 
“I before E except after C”. This rule of thumb advises that when an I 
and an E are adjacent in a word, the I will precede the E, unless they 
are immediately preceded by a C. When preceded by a C the E will appear 
ahead of the I. This advice holds true for words without an immediately 
preceding C such as believe, chief, fierce and friend, and is similarly
true for words with an immediately preceding C such as ceiling and 
receipt. However, there are exceptions to this rule, such as weird.
Create a program that processes a file containing lines of text. Each 
line in the file may contain many words (or no words at all). Any words 
that do not contain an E adjacent to an I should be ignored. Words that 
contain an adjacent E and I (in either order) should be examined to 
determine whether or not they follow the “I before E except after C” 
rule. Construct and report two lists: One that contains all of the words 
that follow the rule, and one that contains all of the words that 
violate the rule. Neither of your lists should contain any repeated 
values. Report the lengths of the lists at the end of your program so 
that one can easily determine the proportion of the words in the file 
that respect the “I before E except after C” rule.
'''
import helpers
helpers.ready_import_outofdir('/Volumes/Data stuffs/Python/LCCL_Python2/PS 5')
from ex133b import isSublist

with open('/Volumes/Data stuffs/Python/LCCL_Python2/PS 7/files/words.txt', 'r') as f:
    lines = f.readlines()

followers = list()
violators = list()

for line in lines:
    word = line.strip()
    if not (isSublist(list(word), ['i', 'e']) or isSublist(list(word), ['e', 'i'])):
        continue
    if isSublist(list(word), ['i', 'e']) or isSublist(list(word), ['c', 'e', 'i']):
        followers.append(word)
        continue
    violators.append(word)

print(f'Followers (length {len(followers)}): {followers}')
print('\n\n\n')
print(f'Violators (length {len(violators)}): {violators}')
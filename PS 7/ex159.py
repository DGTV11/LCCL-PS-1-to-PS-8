'''
While generating a password by selecting random characters usually 
creates one that is relatively secure, it also generally gives a 
password that is difficult to memorize. As an alternative, some systems 
construct a password by taking two English words and concatenating them. 
While this password may not be as secure, it is normally much easier to 
memorize. Write a program that reads a file containing a list of words, 
randomly selects two of them, and concatenates them to produce a new 
password. When producing the password ensure that the total length is 
between 8 and 10 characters, and that each word used is at least three 
letters long. Capitalize each word in the password so that the user can 
easily see where one word ends and the next one begins. Finally, your
program should display the password for the user.
'''

# Read file & save words
with open('/Volumes/Data stuffs/Python/LCCL_Python2/PS 7/files/words.txt', 'r') as f:
    WORDS = f.readlines()

# Imports
from random import choice

# Main generator
i = 0
while True:
    word1 = choice(WORDS).capitalize()[:-1]
    if len(word1) < 3:
        i += 1
        continue
    word2 = choice(WORDS).capitalize()[:-1]
    if len(word2) < 3:
        i += 1
        continue
    out = word1 + word2
    if 8 <= len(out) <= 10:
        print('Password:', out)
        break
    i += 1

print('No. of attempts:', i)
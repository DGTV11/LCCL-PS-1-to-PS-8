'''
• If the word begins with a consonant (including y), then all 
letters at the beginning of the word, up to the first vowel 
(excluding y), are removed and then added to the end of the 
word, followed by ay. For example, computer becomes omputercay 
and think becomes inkthay.

• If the word begins with a vowel (not including y), then way 
is added to the end of the word. For example, algorithm 
becomes algorithmway and office becomes officeway.

Write a program that reads a line of text from the user. 
Then your program should translate the line into Pig Latin and 
display the result. You may assume that the string entered by 
the user only contains lowercase letters and spaces.
'''

VOWELS = ["a", "e", "i", "o", "u"]

def transWord(word):
    if word[0] in VOWELS:
        return f"{word}way"
    else:
        atbackuntilind = int()
        for i, char in enumerate(word):
            if char in VOWELS:
                atbackuntilind = i
                break
        return f"{word[atbackuntilind:]}{word[: atbackuntilind]}ay"

if __name__ == '__main__':
    print("TRANSLATED WORD: " + transWord(input("ORIGINAL WORD: ")))
from ex117 import wordsOnly

sentc = input("Please input a sentence: ")

wo = wordsOnly(sentc.lower())
wox = wo
wo.reverse()

if wox == wo:
    print(f"\"{sentc}\" is a word by word palindrome.")
else:
    print(f"\"{sentc}\" is not a word by word palindrome.")
PUNCTUATION = [",", ".", "?", "!", "'", "\"", ":", ";"]

def wordsOnly(sentc):
    sentc = str(sentc)
    ss = sentc.split()
    for i, word in enumerate(ss):
        if word[-1] in PUNCTUATION:
            ss[i] = ss[i][:-1]
        if word[0] in PUNCTUATION:
            ss[i] = ss[i][1:]

    while "-" in ss:
        ss.remove("-")
    
    return ss

if __name__ == "__main__":
    sentc = input("Please input sentence: ")
    print(wordsOnly(sentc))
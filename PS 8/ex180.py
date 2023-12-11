'''
Let s and t be the strings
If the length of s is 0 then
    Return the length of t
Else if the length of t is 0 then
    Return the length of s
Else
    Set cost to 0
    If the last character in s does not equal the last character in t then
        Set cost to 1
    Set d1 equal to the edit distance between all characters except the last one
        in s, and all characters in t, plus 1
    Set d2 equal to the edit distance between all characters in s, and all
        characters except the last one in t, plus 1
    Set d3 equal to the edit distance between all characters except the last one
        in s, and all characters except the last one in t, plus cost
    Return the minimum of d1, d2 and d3
'''

def recursive_edit_dist_search(s: str, t: str) -> int:
    if len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    else:
        cost: int = 1 if s[-1] != t[-1] else 0
        
        d1: int = recursive_edit_dist_search(s[:-1], t) + 1
        d2: int = recursive_edit_dist_search(s, t[:-1]) + 1
        d3: int = recursive_edit_dist_search(s[:-1], t[:-1]) + cost
    
        return min(d1, d2, d3)
    
if __name__ == '__main__':
    si = input('Please input first string: ')
    ti = input('Please input second string: ')
    print(f"The edit distance between '{si}' and '{ti}' is {recursive_edit_dist_search(si, ti)}")
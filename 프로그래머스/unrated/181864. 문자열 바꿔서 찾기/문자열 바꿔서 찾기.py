import re

def solution(myString, pat):
    change = list()
    for letter in myString:
        if letter == 'A':
            change.append('B')
        elif letter == 'B':
            change.append('A')
        else:
            change.append(letter)
    return 1 if re.search(pat, ''.join(change)) else 0
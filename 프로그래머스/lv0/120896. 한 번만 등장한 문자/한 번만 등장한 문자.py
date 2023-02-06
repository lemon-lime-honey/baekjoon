from collections import Counter

def solution(s):
    letter = Counter(s)
    answer = sorted([x for x in letter if letter[x] == 1])
    return (''.join(answer))
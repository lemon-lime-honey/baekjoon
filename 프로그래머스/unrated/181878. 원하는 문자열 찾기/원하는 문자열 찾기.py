import re

def solution(myString, pat):
    if re.search(pat.lower(), myString.lower()): return 1
    return 0
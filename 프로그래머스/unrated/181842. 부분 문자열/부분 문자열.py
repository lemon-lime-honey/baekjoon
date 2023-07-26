import re

def solution(str1, str2):
    return 1 if re.search(str1, str2) else 0
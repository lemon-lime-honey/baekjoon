import re

def solution(strArr):
    answer = list()
    for string in strArr:
        if re.search('ad', string): continue
        answer.append(string)
    return answer
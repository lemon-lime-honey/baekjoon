import re

def solution(str_list, ex):
    answer = list()
    for string in str_list:
        if re.search(ex, string): continue
        answer.append(string)
    return ''.join(answer)
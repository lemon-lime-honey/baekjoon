import re

def solution(order):
    answer = 0
    for item in order:
        if re.search('cafelatte', item):
            answer += 5000
        else:
            answer += 4500
    return answer
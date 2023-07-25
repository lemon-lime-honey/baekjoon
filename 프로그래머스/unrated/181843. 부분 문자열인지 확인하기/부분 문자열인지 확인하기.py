import re

def solution(my_string, target):
    if re.search(target, my_string):
        return 1
    return 0
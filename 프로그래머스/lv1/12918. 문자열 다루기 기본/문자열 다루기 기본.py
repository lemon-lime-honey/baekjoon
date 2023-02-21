def solution(s):
    length = len(s)
    if length not in (4, 6):
        return False
    for element in s:
        if element.isalpha():
            return False
    return True
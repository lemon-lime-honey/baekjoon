def solution(s):
    num = len(s) // 2
    if len(s) % 2:
        return s[num]
    return s[num - 1: num + 1]
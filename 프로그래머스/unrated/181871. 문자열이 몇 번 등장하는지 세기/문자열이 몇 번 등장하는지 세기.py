def solution(myString, pat):
    answer = 0
    ref = 0
    while ref < len(myString) - len(pat) + 1:
        if myString[ref:ref + len(pat)] == pat: answer += 1
        ref += 1
    return answer
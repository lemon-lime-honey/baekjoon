def solution(myString, pat):
    for i in range(len(myString) - 1, len(pat) - 2, -1):
        if pat == myString[i - len(pat) + 1:i + 1]:
            return myString[:i + 1]
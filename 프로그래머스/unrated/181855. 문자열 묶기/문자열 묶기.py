from collections import defaultdict

def solution(strArr):
    answer = defaultdict(int)
    for string in strArr:
        answer[len(string)] += 1
    return max(answer.values())
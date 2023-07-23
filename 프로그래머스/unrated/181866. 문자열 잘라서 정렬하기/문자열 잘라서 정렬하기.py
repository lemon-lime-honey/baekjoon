def solution(myString):
    raw = myString.split('x')
    answer = list()
    for string in raw:
        if string: answer.append(string)
    return sorted(answer)
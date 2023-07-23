def solution(myString):
    answer = list()
    result = myString.split('x')
    for string in result:
        answer.append(len(string))
    return answer
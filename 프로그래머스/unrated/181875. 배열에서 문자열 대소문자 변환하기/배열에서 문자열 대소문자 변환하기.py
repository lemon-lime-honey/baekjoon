def solution(strArr):
    answer = list()
    for index, letter in enumerate(strArr):
        if index % 2: answer.append(letter.upper())
        else: answer.append(letter.lower())
    return answer
def solution(myString):
    answer = list()
    for letter in myString:
        if letter < 'l': answer.append('l')
        else: answer.append(letter)
    return ''.join(answer)
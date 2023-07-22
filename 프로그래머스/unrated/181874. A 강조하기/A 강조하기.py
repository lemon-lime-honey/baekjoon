def solution(myString):
    answer = list()
    for letter in myString:
        if letter in 'Aa':
            answer.append('A')
        elif letter.isupper():
            answer.append(letter.lower())
        else:
            answer.append(letter)
    return ''.join(answer)
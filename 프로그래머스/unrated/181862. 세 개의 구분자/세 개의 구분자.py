def solution(myStr):
    answer = list()
    for letter in myStr:
        if letter in 'abc':
            answer.append(' ')
        else:
            answer.append(letter)
    result = ''.join(answer).split()
    return result if result else ['EMPTY']
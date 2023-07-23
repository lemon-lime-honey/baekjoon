def solution(rny_string):
    answer = list()
    for letter in rny_string:
        if letter == 'm':
            answer.append('rn')
        else:
            answer.append(letter)
    return ''.join(answer)
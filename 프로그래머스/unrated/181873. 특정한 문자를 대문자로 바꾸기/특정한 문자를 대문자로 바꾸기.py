def solution(my_string, alp):
    answer = list()
    for letter in my_string:
        if letter == alp:
            answer.append(alp.upper())
        else:
            answer.append(letter)
    return ''.join(answer)
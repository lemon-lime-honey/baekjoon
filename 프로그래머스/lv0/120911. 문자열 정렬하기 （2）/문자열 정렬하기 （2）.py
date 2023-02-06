def solution(my_string):
    answer = list()
    
    for letter in my_string:
        answer.append(letter.lower())
    answer.sort()

    return (''.join(answer))
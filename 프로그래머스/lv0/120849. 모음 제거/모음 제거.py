def solution(my_string):
    answer = list()
    for letter in my_string:
        if letter not in 'aeiou':
            answer.append(letter)
    return (''.join(answer))
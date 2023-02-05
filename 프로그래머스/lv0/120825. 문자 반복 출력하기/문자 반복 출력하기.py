def solution(my_string, n):
    answer = list()
    for letter in my_string:
        answer.append(letter * n)
    return (''.join(answer))
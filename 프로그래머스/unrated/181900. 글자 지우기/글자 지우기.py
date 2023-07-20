def solution(my_string, indices):
    answer = list(my_string)
    for index in indices:
        answer[index] = ''
    return ''.join(answer)
def solution(my_string, m, c):
    answer = list()
    for i in range(c - 1, len(my_string), m):
        answer.append(my_string[i])
    return ''.join(answer)
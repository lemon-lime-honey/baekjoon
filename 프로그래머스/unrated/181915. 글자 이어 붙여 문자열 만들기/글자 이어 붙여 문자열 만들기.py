def solution(my_string, index_list):
    answer = list()
    for index in index_list:
        answer.append(my_string[index])
    return ''.join(answer)
def solution(str_list):
    for index, letter in enumerate(str_list):
        if letter == 'l':
            return str_list[:index]
        if letter == 'r':
            return str_list[index + 1:]
    return list()
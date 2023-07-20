def solution(num_list):
    for index, number in enumerate(num_list):
        if number < 0: return index
    return -1
def solution(arr, delete_list):
    delete_set = set(delete_list)
    answer = list()
    for num in arr:
        if num in delete_set:
            delete_set.remove(num)
        else:
            answer.append(num)
    return answer
def solution(arr):
    answer = list()
    for i in range(len(arr)):
        if arr[i] == 2:
            answer = arr[i:]
            break
    else:
        return [-1]
    while answer and answer[-1] != 2:
        answer.pop()
    return answer
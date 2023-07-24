def solution(arr):
    answer = list()
    i = 0
    while i < len(arr):
        if not answer:
            answer.append(arr[i])
        else:
            if answer[-1] == arr[i]:
                answer.pop()
            else:
                answer.append(arr[i])
        i += 1
    return answer if answer else [-1]
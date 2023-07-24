def solution(arr, flag):
    answer = list()
    for index, f in enumerate(flag):
        if f:
            answer.extend([arr[index] for i in range(arr[index] * 2)])
        else:
            for i in range(arr[index]):
                answer.pop()
    return answer
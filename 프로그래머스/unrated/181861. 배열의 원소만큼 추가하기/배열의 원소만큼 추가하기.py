def solution(arr):
    answer = list()
    for num in arr:
        answer.extend([num for i in range(num)])
    return answer
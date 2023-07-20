def solution(start, end):
    answer = list()
    for i in range(start, end - 1, -1):
        answer.append(i)
    return answer
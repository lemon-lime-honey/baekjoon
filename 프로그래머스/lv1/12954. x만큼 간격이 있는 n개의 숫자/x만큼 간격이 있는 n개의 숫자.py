def solution(x, n):
    answer = list()
    for i in range(n):
        answer.append(x * (i + 1))
    return answer
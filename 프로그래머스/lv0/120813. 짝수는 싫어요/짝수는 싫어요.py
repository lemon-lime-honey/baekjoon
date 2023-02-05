def solution(n):
    answer = list()
    for i in range(1, n + 1):
        if i % 2:
            answer.append(i)
    return answer
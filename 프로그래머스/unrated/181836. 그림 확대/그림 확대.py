def solution(picture, k):
    answer = ['' for i in range(len(picture) * k)]
    for i in range(len(picture)):
        for j in range(len(picture[i])):
            for l in range(k * i, k * i + k):
                answer[l] += picture[i][j] * k
    return answer
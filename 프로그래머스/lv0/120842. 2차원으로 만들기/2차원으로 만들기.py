def solution(num_list, n):
    length = len(num_list)
    answer = [[0 for i in range(n)]for j in range(length // n)]

    for i in range(length // n):
        for j in range(n):
            answer[i][j]  = num_list[i * n + j]
    
    return answer
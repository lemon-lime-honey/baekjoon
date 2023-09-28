def solution(n, results):
    result = [[int(1e9) for i in range(n + 1)] for j in range(n + 1)]
    answer = 0

    for a, b in results:
        result[a][b] = 1

    for i in range(1, n + 1):
        result[i][i] = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if result[j][k] > result[j][i] + result[i][k]:
                    result[j][k] = result[j][i] + result[i][k]

    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            if (result[i][j] not in (int(1e9), 0) or
               result[j][i] not in (int(1e9), 0)):
                cnt += 1
        if cnt == n - 1: answer += 1

    return answer
def solution(n, s, a, b, fares):
    costs = [[int(1e9) for i in range(n + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        costs[i][i] = 0

    for start, end, cost in fares:
        costs[start][end] = cost
        costs[end][start] = cost

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if costs[j][k] <= costs[j][i] + costs[i][k]:
                    continue
                costs[j][k] = costs[j][i] + costs[i][k]

    result = int(1e9)

    for i in range(1, n + 1):
        result = min(costs[s][i] + costs[i][a] + costs[i][b], result)
    
    return result
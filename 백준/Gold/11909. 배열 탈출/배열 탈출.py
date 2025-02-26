from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for i in range(n)]
costs = [[int(1e9) for i in range(n)] for j in range(n)]
costs[0][0] = 0

for i in range(1, n):
    if graph[i - 1][0] <= graph[i][0]:
        costs[i][0] = costs[i - 1][0] + graph[i][0] - graph[i - 1][0] + 1
    else:
        costs[i][0] = costs[i - 1][0]
    if graph[0][i - 1] <= graph[0][i]:
        costs[0][i] = costs[0][i - 1] + graph[0][i] - graph[0][i - 1] + 1
    else:
        costs[0][i] = costs[0][i - 1]

for i in range(1, n):
    for j in range(1, n):
        left, top = costs[i][j - 1], costs[i - 1][j]
        if graph[i][j - 1] <= graph[i][j]:
            left += graph[i][j] - graph[i][j - 1] + 1
        if graph[i - 1][j] <= graph[i][j]:
            top += graph[i][j] - graph[i - 1][j] + 1
        costs[i][j] = min(left, top)

print(costs[-1][-1])

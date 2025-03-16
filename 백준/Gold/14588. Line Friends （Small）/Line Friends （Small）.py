import sys

input = sys.stdin.readline

n = int(input())
lines = [list(map(int, input().split())) for i in range(n)]

graph = [[int(1e9) for i in range(n)] for j in range(n)]

for i in range(n):
    graph[i][i] = 0

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if lines[j][1] < lines[i][0] or lines[i][1] < lines[j][0]:
            continue
        graph[i][j] = 1
        graph[j][i] = 1

for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][k] <= graph[j][i] + graph[i][k]:
                continue
            graph[j][k] = graph[j][i] + graph[i][k]

q = int(input())

for i in range(q):
    a, b = map(int, input().split())
    if graph[a - 1][b - 1] == int(1e9):
        print(-1)
    else:
        print(graph[a - 1][b - 1])

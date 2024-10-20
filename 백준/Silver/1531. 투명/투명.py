n, m = map(int, input().split())
graph = [[0 for i in range(101)] for j in range(101)]
result = 0

for i in range(n):
    r1, c1, r2, c2 = map(int, input().split())
    for r in range(r1 - 1, r2):
        for c in range(c1 - 1, c2):
            graph[r][c] += 1

for i in range(101):
    for j in range(101):
        if graph[i][j] > m:
            result += 1

print(result)

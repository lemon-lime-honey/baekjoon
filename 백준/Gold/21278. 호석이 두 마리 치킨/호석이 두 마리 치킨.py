import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [[int(1e9) for i in range(n + 1)] for j in range(n + 1)]
result = [0, 0, int(1e9)]

for i in range(m):
    a, b = map(int, input().split())
    maps[a][b] = 1
    maps[b][a] = 1

for i in range(1, n + 1):
    maps[i][i] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if maps[j][k] <= maps[k][i] + maps[i][j]: continue
            maps[j][k] = maps[k][i] + maps[i][j]

for i in range(1, n):
    for j in range(i + 1, n + 1):
        time = 0
        for k in range(1, n + 1):
            if maps[i][k] <= maps[j][k]:
                time += maps[i][k]
            else:
                time += maps[j][k]
        if time * 2 < result[2]:
            result = [i, j, time * 2]

print(*result)
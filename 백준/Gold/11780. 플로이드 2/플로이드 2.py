import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
info = [[float('inf') for i in range(n + 1)] for j in range(n + 1)]
result = [[[i] for i in range(n + 1)] for j in range(n + 1)]

for i in range(1, n + 1):
    info[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    if info[a][b] < c: continue
    info[a][b] = c

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if info[j][k] <= info[j][i] + info[i][k]:
                continue
            info[j][k] = info[j][i] + info[i][k]
            result[j][k] = result[j][i] + result[i][k]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if info[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(info[i][j], end = ' ')
    print()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if info[i][j] in (0, float('inf')):
            print(0)
        else:
            print(len(result[i][j]) + 1, i, *result[i][j])
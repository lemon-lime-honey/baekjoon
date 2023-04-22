import sys
input = sys.stdin.readline

n, m = map(int, input().split())
marble = [[int(1e9) for i in range(n + 1)] for j in range(n + 1)]
marble_rev = [[int(1e9) for i in range(n + 1)] for j in range(n + 1)]
cnt = 0
cnt_rev = 0
result = 0

for i in range(m):
    a, b = map(int, input().split())
    marble[a][b] = 1
    marble_rev[b][a] = 1

for i in range(1, n + 1):
    marble[i][i] = 0
    marble_rev[i][i] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if marble[j][i] + marble[i][k] < marble[j][k]:
                marble[j][k] = marble[j][i] + marble[i][k]
            if marble_rev[j][i] + marble_rev[i][k] < marble_rev[j][k]:
                marble_rev[j][k] = marble_rev[j][i] + marble_rev[i][k]

for i in range(1, n + 1):
    cnt, cnt_rev = 0, 0
    for j in range(1, n + 1):
        if marble[i][j] not in (0, int(1e9)):
            cnt += 1
        if marble_rev[i][j] not in (0, int(1e9)):
            cnt_rev += 1
    if cnt > n // 2 or cnt_rev > n // 2:
        result += 1

print(result)
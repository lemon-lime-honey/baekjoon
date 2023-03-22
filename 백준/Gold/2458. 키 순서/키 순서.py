import sys
input = sys.stdin.readline

n, m = map(int, input().split())
height = [[0 for i in range(n)] for j in range(n)]
result = 0

for i in range(m):
    a, b = map(int, input().split())
    height[a - 1][b - 1] = 1

for i in range(n):
    for j in range(n):
        for k in range(n):
            if height[j][i] + height[i][k] == 2:
                height[j][k] = 1

for i in range(n):
    cnt = 0
    for j in range(n):
        cnt += height[i][j] + height[j][i]
    if cnt == (n - 1):
        result += 1

print(result)
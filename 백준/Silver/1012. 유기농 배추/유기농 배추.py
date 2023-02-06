import sys

sys.setrecursionlimit(10 ** 6)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(n1, n2):
    farm[n1][n2] = 2

    for i in range(4):
        if (0 <= n2 + dx[i] < m) and (0 <= n1 + dy[i] < n):
            if farm[n1 + dy[i]][n2 + dx[i]] == 1:
                dfs(n1 + dy[i], n2 + dx[i])

t = int(sys.stdin.readline())

for i in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    farm = [[0 for j in range(m)]for l in range(n)]
    result = 0

    for j in range(k):
        x, y = map(int, sys.stdin.readline().split())
        farm[y][x] = 1
    
    for j in range(n):
        for l in range(m):
            if farm[j][l] == 1:
                dfs(j, l)
                result += 1
    
    print(result)
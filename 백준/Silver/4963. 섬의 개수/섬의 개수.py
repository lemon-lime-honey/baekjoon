import sys

sys.setrecursionlimit(100000)

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

def dfs(n, m):
    chart[n][m] = 2
    for i in range(8):
        if (0 <= n + dx[i] < h) and (0 <= m + dy[i] < w):
            if chart[n + dx[i]][m + dy[i]] == 1:
                dfs(n + dx[i], m + dy[i])

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == h == 0:
        break
    chart = [[0 for i in range(w)]for j in range(h)]
    result = 0

    for i in range(h):
        chart[i] = list(map(int, sys.stdin.readline().split()))
    
    for i in range(h):
        for j in range(w):
            if chart[i][j] == 1:
                dfs(i, j)
                result += 1
    
    print(result)
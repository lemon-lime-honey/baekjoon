import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def dfs(r, c):
    if r == m - 1 and c == n - 1:
        return 1

    if dp[r][c] == -1:
        dp[r][c] = 0
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if (0 <= nr < m) and (0 <= nc < n):
                if graph[nr][nc] < graph[r][c]:
                    dp[r][c] += dfs(nr, nc)

    return dp[r][c]


m, n = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(m)]
dp = [[-1 for i in range(n)] for j in range(m)]

print(dfs(0, 0))
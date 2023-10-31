import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs(r, c):
    if dp[r][c] == -1:
        dp[r][c] = 0

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and bamboo[r][c] < bamboo[nr][nc]:
                dp[r][c] = max(dp[r][c], dfs(nr, nc))
    
    return dp[r][c] + 1


dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

n = int(input())
bamboo = [list(map(int, input().split())) for i in range(n)]
dp = [[-1 for i in range(n)] for j in range(n)]
result = 0

for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))

print(result)
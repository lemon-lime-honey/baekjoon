import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = [list(map(int, input().split())) for i in range(n)]
dp = [[0 for i in range(k + 1)] for j in range(n + 1)]

for i in range(n + 1):
    for j in range(k + 1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif items[i - 1][0] <= j:
            dp[i][j] = max(items[i - 1][1] + dp[i - 1][j - items[i - 1][0]], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][k])
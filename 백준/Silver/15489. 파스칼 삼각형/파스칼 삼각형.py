from math import comb

r, c, w = map(int, input().split())

dp = [[0 for i in range(r + w - 1)] for j in range(r + w - 1)]
dp[0][0] = 1
result = 0

for i in range(1, r + w - 1):
    dp[i][0], dp[i][i] = 1, 1

for i in range(1, r + w - 1):
    for j in range(1, i):
        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

for i in range(w):
    for j in range(i + 1):
        result += dp[r - 1 + i][c - 1 + j]

print(result)
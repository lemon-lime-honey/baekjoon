n = int(input())
house = [list(map(int, input().split())) for i in range(n)]
dp = [[[0, 0, 0] for i in range(n)] for j in range(n)]

dp[0][1][0] = 1

for i in range(n):
    for j in range(2, n):
        if house[i][j] == 1: continue
        dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]

        if i == 0: continue
        dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2]

        if house[i - 1][j] or house[i][j - 1]:
            continue
        dp[i][j][2] = sum(dp[i - 1][j - 1])

print(sum(dp[-1][-1]))
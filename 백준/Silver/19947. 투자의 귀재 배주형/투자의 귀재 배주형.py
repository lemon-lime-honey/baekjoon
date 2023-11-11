h, y = map(int, input().split())
dp = [0 for i in range(y + 1)]
dp[0] = h

for i in range(1, y + 1):
    if i < 3:
        dp[i] = int(dp[i - 1] * 1.05)
    elif i < 5:
        dp[i] = max(int(dp[i - 1] * 1.05), int(dp[i - 3] * 1.2))
    else:
        dp[i] = max(
            int(dp[i - 1] * 1.05),
            int(dp[i - 3] * 1.2),
            int(dp[i - 5] * 1.35)
        )

print(dp[-1])
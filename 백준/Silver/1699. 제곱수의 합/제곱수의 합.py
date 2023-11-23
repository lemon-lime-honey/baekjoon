n = int(input())
dp = [int(1e9) for i in range(n + 1)]
dp[0] = 0

for i in range(1, int(n ** 0.5) + 1):
    dp[i * i] = 1

for i in range(1, n + 1):
    chk = int(1e9)
    for j in range(1, int(i ** 0.5) + 1):
        chk = min(chk, dp[j * j] + dp[i - j * j])
    dp[i] = min(dp[i], chk)

print(dp[n])
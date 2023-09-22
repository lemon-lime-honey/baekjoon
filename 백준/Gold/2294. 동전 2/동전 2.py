import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = set()
max_cost = 0

for i in range(n):
    ipt = int(input())
    coins.add(ipt)
    max_cost = max(max_cost, ipt)

dp = [int(1e9) for i in range(max(k + 1, max_cost + 1))]

for coin in coins:
    dp[coin] = 1
    for i in range(coin, k + 1):
        dp[i] = min(dp[i - coin] + 1, dp[i])

print(-1 if dp[k] == int(1e9) else dp[k])
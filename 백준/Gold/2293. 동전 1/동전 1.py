import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for i in range(n)]
dp = [1] + [0 for i in range(k + 1)]

for coin in coins:
    for cost in range(coin, k + 1):
        dp[cost] += dp[cost - coin]

print(dp[k])
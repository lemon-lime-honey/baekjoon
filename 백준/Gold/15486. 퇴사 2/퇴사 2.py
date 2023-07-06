import sys
input = sys.stdin.readline

n = int(input())
works = [list(map(int, input().split())) for i in range(n)]
dp = [0 for i in range(n + 1)]
maximum = 0

for i in range(n):
    maximum = max(maximum, dp[i])
    if i + works[i][0] <= n:
        dp[i + works[i][0]] = max(maximum + works[i][1], dp[i + works[i][0]])

print(max(dp))
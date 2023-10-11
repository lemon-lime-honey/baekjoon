import sys
input = sys.stdin.readline

n = int(input())
p = [0] + list(map(int, input().split()))
dp = [0 for i in range(n + 1)]

for i in range(1, n + 1):
    dp[i] = min(dp[i - j] + p[j] for j in range(1, i + 1))

print(dp[-1])
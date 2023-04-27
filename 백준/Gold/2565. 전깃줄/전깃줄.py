import sys
input = sys.stdin.readline

n = int(input())
cables = sorted([list(map(int, input().split())) for i in range(n)])
dp = [1 for i in range(n)]

for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if cables[i][1] < cables[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
n, s, m = map(int, input().split())
volume = list(map(int, input().split()))
dp = [[False for i in range(m + 1)] for j in range(n)]

if s + volume[0] <= m: dp[0][s + volume[0]] = True
if s - volume[0] >= 0: dp[0][s - volume[0]] = True

for i in range(1, n):
    for j in range(m + 1):
        if not dp[i - 1][j]: continue
        if j + volume[i] <= m:
            dp[i][j + volume[i]] = True
        if j - volume[i] >= 0:
            dp[i][j - volume[i]] = True

result = -1

for i in range(m + 1):
    if dp[-1][i]: result = i

print(result)

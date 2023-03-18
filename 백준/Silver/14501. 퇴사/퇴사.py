n = int(input())

dp = [0 for i in range(n + 1)]
t = list()
p = list()

for i in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)

for i in range(n):
    for j in range(i + t[i], n + 1):
        if dp[j] < dp[i] + p[i]:
            dp[j] = dp[i] + p[i]

print(dp[-1])
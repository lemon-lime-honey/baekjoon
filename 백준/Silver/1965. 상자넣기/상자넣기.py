n = int(input())
box = list(map(int, input().split()))
dp = [0 for i in range(n)]

for i in range(1, n):
    for j in range(i):
        if box[j] < box[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp) + 1)

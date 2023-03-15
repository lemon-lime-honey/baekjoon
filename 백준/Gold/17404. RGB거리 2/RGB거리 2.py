n = int(input())
answer = 10 ** 5
cost = list()
dp = [[0 for i in range(3)] for j in range(n)]

for i in range(n):
    cost.append(list(map(int, input().split())))

for i in range(3):
    dp = [[10 ** 5, 10 ** 5, 10 ** 5] for j in range(n)]
    dp[0][i] = cost[0][i]
    for j in range(1, n):
        dp[j][0] = min(dp[j - 1][1] + cost[j][0], dp[j - 1][2] + cost[j][0])
        dp[j][1] = min(dp[j - 1][0] + cost[j][1], dp[j - 1][2] + cost[j][1])
        dp[j][2] = min(dp[j - 1][0] + cost[j][2], dp[j - 1][1] + cost[j][2])
    for k in range(3):
        if i != k:
            answer = min(answer, dp[-1][k])

print(answer)
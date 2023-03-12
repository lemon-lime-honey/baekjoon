one = input()
two = input()
dp = [[0 for i in range(len(two))] for j in range(len(one))]
result = 0

for i in range(len(one)):
    for j in range(len(two)):
        if one[i] == two[j]:
            if not i or not j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + 1
            result = max(result, dp[i][j])

print(result)
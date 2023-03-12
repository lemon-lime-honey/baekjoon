one = input()
two = input()
three = input()
dp = [[[0 for i in range(len(three) + 1)] for j in range(len(two) + 1)] for k in range(len(one) + 1)]

for i in range(len(one) - 1, -1, -1):
    for j in range(len(two) - 1, -1, -1):
        for k in range(len(three) - 1, -1, -1):
            if one[i] == two[j] == three[k]:
                dp[i][j][k] = dp[i + 1][j + 1][k + 1] + 1
            else:
                dp[i][j][k] = max(dp[i + 1][j][k], dp[i + 1][j + 1][k], dp[i + 1][j][k + 1], dp[i][j + 1][k], dp[i][j + 1][k + 1], dp[i][j][k + 1])

print(dp[0][0][0])
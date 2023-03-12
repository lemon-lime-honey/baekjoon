one = input()
two = input()
dp = [[0 for j in range(len(two) + 1)] for k in range(len(one) + 1)]

for i in range(len(one) - 1, -1, -1):
    for j in range(len(two) - 1, -1, -1):
        if one[i] == two[j]:
            dp[i][j] = dp[i + 1][j + 1] + 1
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
print(dp[0][0])
one = input()
two = input()
dp = [[0 for i in range(len(two) + 1)] for j in range(len(one) + 1)]

for i in range(len(one) - 1, -1, -1):
    for j in range(len(two) - 1, -1, -1):
        if one[i] == two[j]:
            dp[i][j] = dp[i + 1][j + 1] + 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            dp[i][j] = dp[i + 1][j]
        else:
            dp[i][j] = dp[i][j + 1]

r, c = 0, 0
answer = list()

while r < len(one) and c < len(two):
    if dp[r][c] > dp[r + 1][c] and dp[r][c] > dp[r][c + 1]:
        answer.append(one[r])
        r += 1
        c += 1
    elif dp[r][c] > dp[r + 1][c]:
        c += 1
    else:
        r += 1

print(dp[0][0])
print(*answer, sep='')
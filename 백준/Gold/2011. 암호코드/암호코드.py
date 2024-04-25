password = list(map(int, input().rstrip()))
dp = [0 for i in range(len(password) + 1)]
dp[0], dp[1] = 1, 1

if password[0] == 0:
    print(0)
else:
    for i in range(1, len(password)):
        if password[i] != 0:
            dp[i + 1] = (dp[i] + dp[i + 1]) % 1000000
        if 9 < password[i - 1] * 10 + password[i] < 27:
            dp[i + 1] = (dp[i - 1] + dp[i + 1]) % 1000000
    print(dp[-1])
n = int(input())
energy = [list(map(int, input().split())) for i in range(n - 1)]
k = int(input())

if n == 1: print(0)
elif n == 2: print(energy[0][0])
else:
    dp = [[int(1e9), int(1e9)] for i in range(n)]
    dp[0][0] = 0
    dp[1][0] = energy[0][0]
    dp[2][0] = min(dp[0][0] + energy[0][1], dp[1][0] + energy[1][0])

    for i in range(3, n):
        dp[i] = [
            min(
                dp[i - 1][0] + energy[i - 1][0], 
                dp[i - 2][0] + energy[i - 2][1],
            ),
            min(
                dp[i - 3][0] + k,
                dp[i - 1][1] + energy[i - 1][0],
                dp[i - 2][1] + energy[i - 2][1]
            )
        ]

    print(min(dp[-1]))
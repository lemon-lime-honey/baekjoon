import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == m == 0: break

    graph = [list(map(int, input().split())) for i in range(n)]
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
    result = 0

    for i in range(n):
        for j in range(m):
            dp[i + 1][j + 1] = graph[i][j]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == 0: continue
            dp[i][j] = min(
                dp[i - 1][j - 1],
                dp[i - 1][j],
                dp[i][j - 1]
            ) + 1
            result = max(result, dp[i][j])

    print(result)
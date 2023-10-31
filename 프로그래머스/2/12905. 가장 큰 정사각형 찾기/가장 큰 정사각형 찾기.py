def solution(board):
    row, col = len(board), len(board[0])
    dp = [[0 for i in range(col + 1)] for j in range(row + 1)]
    result = 0

    for i in range(row):
        for j in range(col):
            dp[i + 1][j + 1] =  board[i][j]

    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if dp[i][j] == 0: continue
            dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
            result = max(result, dp[i][j])

    return result * result
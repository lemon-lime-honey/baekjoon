def solution(board, k):
    r = len(board)
    c = len(board[0])
    answer = 0
    for i in range(r):
        for j in range(c):
            if i + j <= k:
                answer += board[i][j]
    return answer
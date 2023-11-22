def solution(board, moves):
    basket = list()
    n = len(board)
    answer = 0

    for move in moves:
        for i in range(n):
            if board[i][move - 1] != 0:
                if basket and board[i][move - 1] == basket[-1]:
                    board[i][move - 1] = 0
                    basket.pop()
                    answer += 2
                    break
                basket.append(board[i][move - 1])
                board[i][move - 1] = 0
                break

    return answer
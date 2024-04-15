from copy import deepcopy
import sys
input = sys.stdin.readline


def move(cnt, board):
    if cnt == 5:
        global result
        max_number = max(map(max, board))
        if result < max_number:
            result = max_number
        return

    for i in range(4):
        copied = deepcopy(board)
        move(cnt + 1, direction[i](copied))


def left(board):
    for i in range(n):
        pos = 0
        for j in range(n):
            if board[i][j] == 0: continue
            target = board[i][j]
            board[i][j] = 0

            if board[i][pos] == 0:
                board[i][pos] = target
            elif board[i][pos] == target:
                board[i][pos] += target
                pos += 1
            else:
                pos += 1
                board[i][pos] = target
                
    return board


def right(board):
    for i in range(n):
        pos = n - 1
        for j in range(n - 1, -1, -1):
            if board[i][j] == 0: continue
            target = board[i][j]
            board[i][j] = 0

            if board[i][pos] == 0:
                board[i][pos] = target
            elif board[i][pos] == target:
                board[i][pos] += target
                pos -= 1
            else:
                pos -= 1
                board[i][pos] = target

    return board


def up(board):
    for i in range(n):
        pos = 0
        for j in range(n):
            if board[j][i] == 0: continue
            target = board[j][i]
            board[j][i] = 0

            if board[pos][i] == 0:
                board[pos][i] = target
            elif board[pos][i] == target:
                board[pos][i] += target
                pos += 1
            else:
                pos += 1
                board[pos][i] = target

    return board


def down(board):
    for i in range(n):
        pos = n - 1
        for j in range(n - 1, -1, -1):
            if board[j][i] == 0: continue
            target = board[j][i]
            board[j][i] = 0

            if board[pos][i] == 0:
                board[pos][i] = target
            elif board[pos][i] == target:
                board[pos][i] += target
                pos -= 1
            else:
                pos -= 1
                board[pos][i] = target

    return board


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input().split())) for i in range(n)]
    direction = {0: left, 1: right, 2: up, 3: down}
    result = 0

    move(0, board)

    print(result)
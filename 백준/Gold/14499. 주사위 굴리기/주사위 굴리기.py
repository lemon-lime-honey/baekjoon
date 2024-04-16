import sys
input = sys.stdin.readline


def roll(command):
    global dice
    up, one, two, three, four, down = dice
    if command == 1:
        dice = [four, one, up, three, down, two]
    elif command == 2:
        dice = [two, one, down, three, up, four]
    elif command == 3:
        dice = [one, down, two, up, four, three]
    else:
        dice = [three, up, two, down, four, one]


n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for i in range(n)]
commands = list(map(int, input().split()))
dice = [0 for i in range(6)]
result = list()

dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

for command in commands:
    x += dx[command - 1]
    y += dy[command - 1]
    
    if x < 0 or x >= n or y < 0 or y >= m:
        x -= dx[command - 1]
        y -= dy[command - 1]
        continue

    roll(command)

    if board[x][y] == 0:
        board[x][y] = dice[-1]
    else:
        dice[-1] = board[x][y]
        board[x][y] = 0

    result.append(dice[0])

print(*result, sep='\n')
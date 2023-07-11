from collections import deque
import sys
input = sys.stdin.readline

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

n = int(input())
k = int(input())
board = [[0 for i in range(n)] for j in range(n)]
snake = deque([[0, 0]])
direction = 0
movement = deque()
board[0][0] = 1

for i in range(k):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 2

l = int(input())
time = 0

for i in range(l):
    ipt = list(input().rstrip().split())
    movement.append((int(ipt[0]), ipt[1]))

while True:
    if movement:
        if time == movement[0][0]:
            if movement[0][1] == 'L':
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4
            movement.popleft()
    r, c = snake[0][0] + directions[direction][0], snake[0][1] + directions[direction][1]
    if (0 <= r < n) and (0 <= c < n):
        if board[r][c] == 2:
            snake.appendleft([r, c])
            board[r][c] = 1
        elif board[r][c] == 1:
            time += 1
            break
        else:
            snake.appendleft([r, c])
            board[r][c] = 1
            tail = snake.pop()
            board[tail[0]][tail[1]] = 0
    else:
        time += 1
        break
    time += 1

print(time)
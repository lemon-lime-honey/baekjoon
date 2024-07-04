import sys
input = sys.stdin.readline

dr = [0, 0, 1, 1, 1, -1, -1, -1]
dc = [1, -1, 0, 1, -1, 0, 1, -1]

while True:
    r, c = map(int, input().split())
    if r == c == 0:
        break
    result = [[0 for i in range(c)] for j in range(r)]
    maps = list()
    mines = list()

    for i in range(r):
        maps.append(input().rstrip())
        for j in range(c):
            if maps[i][j] == "*":
                mines.append((i, j))

    for row, col in mines:
        result[row][col] = -1
        for i in range(8):
            nr, nc = row + dr[i], col + dc[i]
            if nr < 0 or nc < 0 or nr >= r or nc >= c or maps[nr][nc] == "*":
                continue
            result[nr][nc] += 1

    for i in range(r):
        for j in range(c):
            print(result[i][j] if result[i][j] != -1 else '*', end='')
        print()

import sys
input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def spread(dust):
    while dust:
        r, c = dust.pop()
        cnt = 0
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if (0 <= nr < row) and (0 <= nc < col):
                if room[nr][nc] != -1:
                    result[nr][nc] += room[r][c] // 5
                    cnt += 1
        if cnt: room[r][c] -= (room[r][c] // 5) * cnt


def purify(rev):
    temp = 0
    if rev:
        for i in range(1, col):
            room[purifier[1]][i], temp = temp, room[purifier[1]][i]
        for i in range(purifier[1] + 1, row):
            room[i][col - 1], temp = temp, room[i][col - 1]
        for i in range(col - 2, -1, -1):
            room[row - 1][i], temp = temp, room[row - 1][i]
        for i in range(row - 2, purifier[1], -1):
            room[i][0], temp = temp, room[i][0]
    else:
        for i in range(1, col):
            room[purifier[0]][i], temp = temp, room[purifier[0]][i]
        for i in range(purifier[0] - 1, -1, -1):
            room[i][col - 1], temp = temp, room[i][col - 1]
        for i in range(col - 2, -1, -1):
            room[0][i], temp = temp, room[0][i]
        for i in range(1, purifier[0]):
            room[i][0], temp = temp, room[i][0]


row, col, t = map(int, input().split())
room = [list(map(int, input().split())) for i in range(row)]
purifier = list()
dust = list()

for i in range(row):
    if room[i][0] == -1:
        purifier.append(i)

for i in range(t):
    for j in range(row):
        for k in range(col):
            if room[j][k] not in (-1, 0):
                dust.append((j, k))
    result = [[0 for i in range(col)] for j in range(row)]
    spread(dust)
    for j in range(row):
        for k in range(col):
            if result[j][k]: room[j][k] += result[j][k]
    purify(False)
    purify(True)

print(sum(map(sum, room)) + 2)
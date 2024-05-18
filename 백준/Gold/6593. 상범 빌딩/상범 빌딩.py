from collections import deque
import sys
input = sys.stdin.readline

mvmt = [(0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]

while True:
    l, r, c = map(int, input().split())
    if l == r == c == 0: break
    building = list()
    que = deque()
    end = None

    for i in range(l):
        floor = list()
        for j in range(r):
            floor.append(input().rstrip())
            if not que or not end:
                for k in range(c):
                    if not que and floor[j][k] == 'S':
                        que.append((i, j, k))
                    if not end and floor[j][k] == 'E':
                        end = (i, j, k)
        building.append(floor)
        input()

    chk = [[[int(1e9) for i in range(c)] for j in range(r)] for k in range(l)]
    chk[que[0][0]][que[0][1]][que[0][2]] = 0

    while que:
        h, row, col = que.popleft()
        if h == end[0] and row == end[1] and col == end[2]:
            break
        for i in range(6):
            nh, nr, nc = h + mvmt[i][0], row + mvmt[i][1], col + mvmt[i][2]
            if (nh < 0 or nr < 0 or nc < 0 or
                nh >= l or nr >= r or nc >= c or
                building[nh][nr][nc] == '#' or
                chk[nh][nr][nc] != int(1e9)):
                continue
            chk[nh][nr][nc] = chk[h][row][col] + 1
            que.append((nh, nr, nc))

    result = chk[end[0]][end[1]][end[2]]

    if result == int(1e9):
        print('Trapped!')
    else:
        print(f'Escaped in {result} minute(s).')

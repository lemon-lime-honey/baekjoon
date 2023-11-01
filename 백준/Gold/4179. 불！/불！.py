from collections import deque
import heapq, sys
input = sys.stdin.readline


def bfs(row, col, flag):
    que = deque([(row, col)])

    if flag: esc[row][col] = 1
    else: burn[row][col] = 1

    while que:
        x, y = que.popleft()

        for i in range(4):
            nr, nc = x + dr[i], y + dc[i]
            if (0 <= nr < r and
                0 <= nc < c and
                maze[nr][nc] != '#'):
                if (flag and esc[nr][nc] == 0 and
                    (esc[x][y] + 1 < burn[nr][nc] or
                    burn[nr][nc] == 0)):
                    esc[nr][nc] = esc[x][y] + 1
                    que.append((nr, nc))
                if not flag:
                    if burn[nr][nc] == 0 or burn[x][y] + 1 < burn[nr][nc]:
                        burn[nr][nc] = burn[x][y] + 1
                        que.append((nr, nc))
            if (flag and (nr == r or nc == c or nr == -1 or nc == -1) and
                (esc[x][y] < burn[x][y] or burn[x][y] == 0)):
                return esc[x][y]


dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

r, c = map(int, input().split())
person = [-1, -1]
fire = list()
maze = list()

for i in range(r):
    ipt = input().rstrip()
    maze.append(ipt)
    for j in range(c):
        if ipt[j] == 'J':
            person = [i, j]
        elif ipt[j] == 'F':
            fire.append((i, j))

esc = [[0 for i in range(c)] for j in range(r)]
burn = [[0 for i in range(c)] for j in range(r)]

if fire:
    for f in fire:
        bfs(*f, False)
chk = bfs(*person, True)

print(chk if chk else 'IMPOSSIBLE')
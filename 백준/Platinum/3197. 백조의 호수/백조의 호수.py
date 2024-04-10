from collections import deque
import sys
input = sys.stdin.readline


def melt():
    while water_now:
        r, c = water_now.popleft()
        lake[r][c] = '.'

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if (nr < 0 or nr >= row or
                nc < 0 or nc >= col or
                water[nr][nc]):
                continue
            if lake[nr][nc] == 'X':
                water_next.append((nr, nc))
            elif lake[nr][nc] == '.':
                water_now.append((nr, nc))
            water[nr][nc] = True


def chk():
    while swan_now:
        r, c = swan_now.popleft()
        if r == target[0] and c == target[1]:
            return True

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= row or nc < 0 or nc >= col or visited[nr][nc]:
                continue
            if lake[nr][nc] == 'X':
                swan_next.append((nr, nc))
            elif lake[nr][nc] == '.':
                swan_now.append((nr, nc))
            visited[nr][nc] = True

    return False


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

row, col = map(int, input().split())
visited = [[False for i in range(col)] for j in range(row)]
water = [[False for i in range(col)] for j in range(row)]
target = [0, 0]
water_now = deque()
water_next = deque()
swan_now = deque()
swan_next = deque()
lake = list()
result = 0

for i in range(row):
    lake.append(list(input().rstrip()))

    for j in range(col):
        if lake[-1][j] == 'L':
            water_now.append((i, j))
            water[i][j] = True
            lake[-1][j] = '.'
            if not swan_now:
                swan_now.append((i, j))
                visited[i][j] = True
            else:
                target = [i, j]
        elif lake[-1][j] == '.':
            water_now.append((i, j))
            water[i][j] = True

while True:
    melt()
    if chk():
        print(result)
        break
    water_now = water_next
    swan_now = swan_next
    water_next = deque()
    swan_next = deque()
    result += 1

from collections import deque

dr = [0, 0, -1, 1, -1, 1, -1, 1]
dc = [1, -1, 0, 0, -1, 1, 1, -1]

n, m = map(int, input().split())
space = list()
shark = list()

for i in range(n):
    space.append(list(map(int, input().split())))
    for j in range(m):
        if space[i][j]: shark.append((i, j))

for row, col in shark:
    que = deque([(row, col)])

    while que:
        r, c = que.popleft()
        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]
            if (0 <= nr < n) and (0 <= nc < m) and space[nr][nc] != 1:
                if space[nr][nc] == 0:
                    space[nr][nc] = space[r][c] + 1
                    que.append((nr, nc))
                else:
                    if space[nr][nc] > space[r][c] + 1:
                        space[nr][nc] = space[r][c] + 1
                        que.append((nr, nc))

print(max(map(max, space)) - 1)
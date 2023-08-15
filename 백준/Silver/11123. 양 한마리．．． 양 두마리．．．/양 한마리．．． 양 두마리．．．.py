from collections import deque


def bfs(row, col):
    que = deque([(row, col)])
    visited[row][col] = True

    while que:
        r, c = que.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if ((0 <= nr < h) and 
                (0 <= nc < w) and
                not visited[nr][nc] and
                ground[nr][nc] == '#'):
                visited[nr][nc] = True
                que.append((nr, nc))


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

t = int(input())

for i in range(t):
    h, w = map(int, input().split())
    visited = [[False for j in range(w)] for k in range(h)]
    ground = list()
    result = 0

    for j in range(h):
        ground.append(list(input()))

    for j in range(h):
        for k in range(w):
            if ground[j][k] == '#' and not visited[j][k]:
                bfs(j, k)
                result += 1

    print(result)
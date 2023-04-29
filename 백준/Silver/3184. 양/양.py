from collections import deque

r, c = map(int, input().split())
graph = [input() for i in range(r)]
visited = [[False for i in range(c)] for j in range(r)]
wolf, sheep = 0, 0
morning = list()
que = deque()

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

for i in range(r):
    for j in range(c):
        if not visited[i][j]:
            que.append((i, j))
            wolf, sheep = 0, 0
            if graph[i][j] == 'v': wolf += 1
            elif graph[i][j] == 'o': sheep += 1
            visited[i][j] = True
            while que:
                row, col = que.popleft()
                for k in range(4):
                    nr, nc = row + dr[k], col + dc[k]
                    if (0 <= nr < r) and (0 <= nc < c):
                        if not visited[nr][nc]:
                            visited[nr][nc] = True
                            if graph[nr][nc] == '#': continue
                            que.append((nr, nc))
                            if graph[nr][nc] == 'v':
                                wolf += 1
                            elif graph[nr][nc] == 'o':
                                sheep += 1
            if wolf >= sheep: morning.append((wolf, 0))
            else: morning.append((0, sheep))

wolf, sheep = 0, 0

for w, s in morning:
    wolf += w
    sheep += s

print(sheep, wolf)
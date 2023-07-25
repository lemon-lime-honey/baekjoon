from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def bfs(row, col):
    que = deque()
    que.append((row, col))
    visited = [[-1 for i in range(n)] for j in range(n)]
    visited[row][col] = 0
    fishes = list()
    while que:
        r, c = que.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if (0 <= nr < n) and (0 <= nc < n) and visited[nr][nc] == -1:
                if ocean[nr][nc] > size: continue
                visited[nr][nc] = visited[r][c] + 1
                que.append((nr, nc))
                if ocean[nr][nc] and ocean[nr][nc] < size:
                    fishes.append((ocean[nr][nc], nr, nc, visited[nr][nc]))
    if fishes:
        fishes.sort(key=lambda x: (x[3], x[1], x[2]))
    return fishes


n = int(input())
ocean = list()
shark = list()
size, cnt = 2, 0
time = 0

for i in range(n):
    ocean.append(list(map(int, input().split())))
    if not shark:
        for j in range(n):
            if ocean[i][j] == 9:
                shark.extend([i, j])
                ocean[i][j] = 0

while True:
    fishes = bfs(shark[0], shark[1])
    if not fishes: break
    time += fishes[0][3]
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0
    shark = [fishes[0][1], fishes[0][2]]
    ocean[fishes[0][1]][fishes[0][2]] = 0

print(time)
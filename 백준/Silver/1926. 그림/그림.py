from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(row, col):
    global cnt
    que = deque([(row, col)])

    while que:
        r, c = map(int, que.pop())
        if paper[r][c] == 1:
            paper[r][c] = 2
            cnt += 1
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if (0 <= nr < n) and (0 <= nc < m) and paper[nr][nc] == 1:
                    que.appendleft((nr, nc))

n, m = map(int, input().split())
paper = [[0 for i in range(m)] for j in range(n)]
result, picture = 0, 0

for i in range(n):
    paper[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1:
            cnt = 0
            picture += 1
            bfs(i, j)
            result = max(result, cnt)

print(picture)
print(result)
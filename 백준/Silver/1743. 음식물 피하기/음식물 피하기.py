from collections import deque

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs(row, col):
    global cnt
    que = deque([[row, col]])

    while que:
        now = que.popleft()
        for i in range(4):
            del_r = now[0] + dr[i]
            del_c = now[1] + dc[i]
            if (0 < del_r <= n) and (0 < del_c <= m):
                if hallway[del_r][del_c] == 1 and not visited[del_r][del_c]:
                    visited[del_r][del_c] = True
                    cnt += 1
                    que.append([del_r, del_c])

n, m, k = map(int, input().split())
hallway = [[0 for i in range(m + 1)] for j in range(n + 1)]
visited = [[False for i in range(m + 1)] for j in range(n + 1)]
result = 0

for i in range(k):
    r, c = map(int, input().split())
    hallway[r][c] = 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if hallway[i][j] and not visited[i][j]:
            cnt = 0
            bfs(i, j)
            result = max(result, cnt)

print(result)
from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def bfs(row, col, ref):
    que = deque()
    que.append((row, col))
    visited[row][col] = True
    graph[row][col] = ref
    result = 1

    while que:
        r, c = que.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc] and not graph[nr][nc]:
                    visited[nr][nc] = True
                    que.append((nr, nc))
                    graph[nr][nc] = ref
                    result += 1

    return result


n, m = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for i in range(n)]
visited = [[False for i in range(m)] for j in range(n)]
answer = [[0 for i in range(m)] for j in range(n)]
cnt = [0, 0]
ref = 2

for i in range(n):
    for j in range(m):
        if not graph[i][j] and not visited[i][j]:
            number = bfs(i, j, ref)
            cnt.append(number)
            ref += 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            answer[i][j] = 1
            chk = set()
            for k in range(4):
                ni, nj = i + dr[k], j + dc[k]
                if 0 <= ni < n and 0 <= nj < m:
                    if graph[ni][nj] != 1:
                        chk.add(graph[ni][nj])
            for num in chk:
                answer[i][j] += cnt[num]
            answer[i][j] %= 10

for i in range(n):
    print(*answer[i], sep='')
from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def bfs():
    que = deque([[0, 0, 0]])
    visited[0][0][0] = 1

    while que:
        r, c, h = que.popleft()
        if r == n - 1 and c == m - 1:
            return visited[r][c][h]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if (0 <= nr < n) and (0 <= nc < m):
                if not space[nr][nc] and not visited[nr][nc][h]:
                    visited[nr][nc][h] = visited[r][c][h] + 1
                    que.append([nr, nc, h])
                elif space[nr][nc] and not h:
                    visited[nr][nc][1] = visited[r][c][0] + 1
                    que.append([nr, nc, 1])
    
    return -1

n, m = map(int, input().split())
space = [list(map(int, input().rstrip())) for i in range(n)]
visited = [[[0 for i in range(2)] for j in range(m)] for k in range(n)]

print(bfs())
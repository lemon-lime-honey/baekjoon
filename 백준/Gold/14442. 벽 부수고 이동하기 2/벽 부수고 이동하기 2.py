from collections import deque
import sys
input = sys.stdin.readline

def dfs():
    result = [[[0 for i in range(k + 1)] for j in range(m)] for l in range(n)]
    que = deque([[0, 0, 0]])
    result[0][0][0] = 1

    while que:
        r, c, h = que.popleft()
        if r == n - 1 and c == m - 1:
            return result[r][c][h]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (0 <= nr < n) and (0 <= nc < m):
                if not graph[nr][nc] and not result[nr][nc][h]:
                    result[nr][nc][h] = result[r][c][h] + 1
                    que.append([nr, nc, h])
                elif graph[nr][nc] and (h < k) and not result[nr][nc][h + 1]:
                    result[nr][nc][h + 1] = result[r][c][h] + 1
                    que.append([nr, nc, h + 1])
    
    return -1

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

n, m, k = map(int, input().split())
graph = [list(map(int, input().rstrip())) for i in range(n)]
print(dfs())
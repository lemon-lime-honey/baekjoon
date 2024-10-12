from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    visited = [[False for i in range(m)] for j in range(n)]
    que = deque([(0, 0, 0)])
    visited[0][0] = True
    result = int(1e9)

    while que:
        dist, r, c = que.popleft()

        if castle[r][c] == 2:
            result = dist + n - r - 1 + m - c - 1
            continue

        if r == n - 1 and c == m - 1:
            return min(result, dist)

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if (
                0 > nr
                or 0 > nc
                or nr >= n
                or nc >= m
                or visited[nr][nc]
                or castle[nr][nc] == 1
            ):
                continue

            que.append((dist + 1, nr, nc))
            visited[nr][nc] = True

    return result


dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

n, m, t = map(int, input().split())
castle = [list(map(int, input().split())) for i in range(n)]
result = bfs()

print(result if result <= t else "Fail")

from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    chk = [[[False for i in range(k + 1)] for j in range(w)] for l in range(h)]
    que = deque([(0, 0, 0, 0)])
    chk[0][0][0] = True
    
    while que:
        r, c, s, m = que.popleft()
        if r == h - 1 and c == w - 1:
            return m

        for dr, dc in rhombus:
            nr, nc = r + dr, c + dc
            if (0 <= nr < h and 0 <= nc < w and
                not chk[nr][nc][s] and
                maps[nr][nc] == 0):
                chk[nr][nc][s] = True
                que.append((nr, nc, s, m + 1))

        if s < k:
            for dr, dc in horse:
                nr, nc = r + dr, c + dc
                if (0 <= nr < h and 0 <= nc < w and
                    not chk[nr][nc][s + 1] and
                    maps[nr][nc] == 0):
                    chk[nr][nc][s + 1] = True
                    que.append((nr, nc, s + 1, m + 1))

    return -1


horse = ((-1, -2), (-2, -1), (-1, 2), (-2, 1),
         (1, -2), (2, -1), (1, 2), (2, 1))

rhombus = ((1, 0), (-1, 0), (0, 1), (0, -1))

k = int(input())
w, h = map(int, input().split())
maps = [list(map(int, input().split())) for i in range(h)]
print(bfs())

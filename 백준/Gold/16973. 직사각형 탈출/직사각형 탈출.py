from collections import deque
import sys
input = sys.stdin.readline


def chk(r, c):
    for i in range(r, r + h + 1):
        if board[i][c] == 1 or board[i][c + w] == 1:
            return False
    for i in range(c, c + w + 1):
        if board[r][i] == 1 or board[r + h][i] == 1:
            return False
    return True


dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for i in range(n)]
h, w, sr, sc, fr, fc = map(int, input().split())
h -= 1
w -= 1
sr -= 1
sc -= 1
fr -= 1
fc -= 1

result = [[int(1e9) for i in range(m)] for j in range(n)]
que = deque([(sr, sc)])
result[sr][sc] = 0

while que:
    r, c = que.popleft()
    if r == fr and c == fc: break
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if (0 > nr or n - h <= nr or 0 > nc or m - w <= nc or
            not chk(nr, nc) or
            result[nr][nc] != int(1e9)):
            continue
        result[nr][nc] = result[r][c] + 1
        que.append((nr, nc))

print(result[fr][fc] if result[fr][fc] != int(1e9) else -1)
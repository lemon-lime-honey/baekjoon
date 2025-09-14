from collections import deque


def search(rr, cc, val):
    find(rr, cc, val)

    while que:
        r, c = que.popleft()

        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if mount[nr][nc] > val:
                que.clear()
                return False

    return True


def find(r, c, val):
    que.append((r, c))
    chk[r][c] = True

    for i in range(8):
        nr, nc = r + dr[i], c + dc[i]
        if (
            nr < 0
            or nr >= n
            or nc < 0
            or nc >= m
            or mount[nr][nc] != val
            or chk[nr][nc]
        ):
            continue
        find(nr, nc, val)


dr = [0, 0, 1, 1, 1, -1, -1, -1]
dc = [-1, 1, -1, 0, 1, -1, 0, 1]

n, m = map(int, input().split())
mount = [list(map(int, input().split())) for i in range(n)]
chk = [[False for i in range(m)] for j in range(n)]
que = deque()
result = 0

for i in range(n):
    for j in range(m):
        if chk[i][j]:
            continue
        if search(i, j, mount[i][j]):
            result += 1

print(result)

import sys
input = sys.stdin.readline


def dfs(r, c, flag):
    chk[r][c] = flag
    nr, nc = r + direction[graph[r][c]][0], c + direction[graph[r][c]][1]

    if not chk[nr][nc]:
        dfs(nr, nc, flag)
    elif chk[nr][nc] == flag:
        global result
        result += 1
        return
    else: return


n, m = map(int, input().split())
graph = [list(input().rstrip()) for i in range(n)]
chk = [[0 for i in range(m)] for j in range(n)]
direction = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
flag, result = 1, 0

for i in range(n):
    for j in range(m):
        if chk[i][j] == 0:
            dfs(i, j, flag)
            flag += 1

print(result)
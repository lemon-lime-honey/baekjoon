import sys
input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]

n, m = map(int, input().split())
chk = [[False for i in range(m)] for j in range(n)]
campus = list()
stack = list()
result = 0

for i in range(n):
    ipt = list(input().strip())
    campus.append(ipt)

    if not stack:
        for j in range(m):
            if ipt[j] == 'I':
                chk[i][j] = True
                stack.append((i, j))

while stack:
    r, c = stack.pop()
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if (0 <= nr < n) and (0 <= nc < m):
            if not chk[nr][nc] and campus[nr][nc] != 'X':
                chk[nr][nc] = True
                stack.append((nr, nc))
                if campus[nr][nc] == 'P': result += 1

print('TT' if result == 0 else result)
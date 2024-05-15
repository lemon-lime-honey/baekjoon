from collections import deque
import sys
input = sys.stdin.readline


def bfs(row, col, flag):
    que = deque([(row, col, 0)])

    while que:
        r, c, num = que.popleft()
        if chk[r][c] < num: continue
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < h and 0 <= nc < w:
                if maps[nr][nc] in '.@' and num + 1 < chk[nr][nc]:
                    chk[nr][nc] = num + 1
                    que.append((nr, nc, num + 1))
            elif flag: return num + 1

    return -1


dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

t = int(input())

for i in range(t):
    w, h = map(int, input().split())
    chk = [[int(1e9) for i in range(w)] for j in range(h)]
    maps = list()
    fire = list()
    mark = None

    for j in range(h):
        maps.append(list(input().rstrip()))
        for k in range(w):
            if not mark and maps[j][k] == '@':
                mark = (j, k)
            elif maps[j][k] == '*':
                fire.append((j, k))
                chk[j][k] = 0

    if fire:
        for f in fire:
            bfs(*f,  False)
    result = bfs(*mark, True)

    maps.clear()
    chk.clear()
    
    print(result if result != -1 else 'IMPOSSIBLE')
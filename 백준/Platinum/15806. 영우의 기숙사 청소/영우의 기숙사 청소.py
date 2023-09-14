from collections import deque
import sys
input = sys.stdin.readline

n, m, k, t = map(int, input().split())
mold = deque([tuple(map(int, input().split())) for i in range(m)])
targets = set(tuple(map(int, input().split())) for i in range(k))
visited = [[[False, False] for i in range(n + 1)] for j in range(n + 1)]
flag = False

dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

for i in range(1, t + 1):
    num = len(mold)
    temp = set()

    for j in range(num):
        r, c = mold.popleft()
        for l in range(8):
            nr, nc = r + dr[l], c + dc[l]
            if 0 < nr < n + 1 and 0 < nc < n + 1:
                if not visited[nr][nc][i % 2] and (nr, nc) not in temp:
                    visited[nr][nc][i % 2] = True
                    temp.add((nr, nc))
                    mold.append((nr, nc))
                if i % 2 == t % 2:
                    if (nr, nc) in targets:
                        print('YES')
                        sys.exit()

print('NO')
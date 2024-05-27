from collections import deque
import heapq, sys
input = sys.stdin.readline


def getDist(points):
    result = [[[int(1e9) for i in range(n)] for j in range(n)] for k in range(m)]

    for idx, point in enumerate(points):
        result[idx][point[0]][point[1]] = 0
        que = deque([(point[0], point[1], 0)])

        while que:
            r, c, d = que.popleft()
            if result[idx][r][c] < d: continue
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if (nr < 0 or nc < 0 or
                    nr >= n or nc >= n or
                    result[idx][nr][nc] != int(1e9) or
                    maps[nr][nc] == 1):
                    continue
                result[idx][nr][nc] = d + 1
                que.append((nr, nc, d + 1))

    return result


dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

n, m, f = map(int, input().split())
maps = [list(map(int, input().split())) for i in range(n)]
cab = list(map(int, input().split()))

cab[0] -= 1
cab[1] -= 1

start = list()
end = list()

for i in range(m):
    a, b, c, d = map(int, input().split())
    start.append((a - 1, b - 1))
    end.append((c - 1, d - 1))

src = getDist(start)
dst = getDist(end)

fin = [False for i in range(m)]
success = True

while True:
    for customer in fin:
        if not customer: break
    else:
        break

    target = list()

    for i in range(m):
        if fin[i]: continue
        heapq.heappush(target,
                       (src[i][cab[0]][cab[1]],
                        start[i][0], start[i][1],
                        end[i][0], end[i][1], i))

    cost = dst[target[0][5]][target[0][1]][target[0][2]]
    nf = f - target[0][0] + cost

    if nf <= 0 or f < target[0][0] + cost:
        success = False
        break

    f = nf
    fin[target[0][5]] = True
    cab = [target[0][3], target[0][4]]

print(f if success else -1)
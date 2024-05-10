import heapq, sys
input = sys.stdin.readline


def dijkstra(row, col):
    que = list()
    heapq.heappush(que, (0, row, col))
    result = [[int(1e9) for i in range(m)] for j in range(n)]
    result[row][col] = 0

    while que:
        time, r, c = heapq.heappop(que)
        if result[r][c] < time: continue
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if (0 > nr or nr >= n or
                0 > nc or nc >= m or
                abs(maps[nr][nc] - maps[r][c]) > t):
                continue
            next_time = 0
            if maps[nr][nc] <= maps[r][c]:
                next_time = time + 1
            else:
                next_time = time + (maps[r][c] - maps[nr][nc]) ** 2

            if next_time < result[nr][nc]:
                result[nr][nc] = next_time
                heapq.heappush(que, (next_time, nr, nc))

    return result


n, m, t, d = map(int, input().split())
maps = [[] for i in range(n)]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

for i in range(n):
    ipt = input().rstrip()
    for j in range(m):
        if ipt[j] <= 'Z':
            maps[i].append(ord(ipt[j]) - 65)
        else:
            maps[i].append(ord(ipt[j]) - 71)

forward = dijkstra(0, 0)
targets = list()

for i in range(n):
    for j in range(m):
        if forward[i][j] <= d:
            heapq.heappush(targets, (-maps[i][j], i, j))

while targets:
    time, r, c = heapq.heappop(targets)
    backward = dijkstra(r, c)
    if forward[r][c] + backward[0][0] <= d:
        print(maps[r][c])
        break
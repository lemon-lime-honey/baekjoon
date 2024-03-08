from collections import defaultdict, deque
import heapq, sys
input = sys.stdin.readline


def get_islands():
    num = 1
    que = deque()
    chk = [[False for i in range(m)] for j in range(n)]

    for i in range(n):
        for j in range(m):
            if chk[i][j] or maps[i][j] == 0: continue
            maps[i][j] = num
            chk[i][j] = True
            que.append((i, j))

            while que:
                r, c = que.popleft()
                flag = False
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if ((nr < 0 or nr >= n) or
                        (nc < 0 or nc >= m) or
                        (chk[nr][nc])): continue
                    if maps[nr][nc] == 0:
                        flag = True
                    else:
                        maps[nr][nc] = num
                        chk[nr][nc] = True
                        que.append((nr, nc))
                if flag: isleDict[num].add((r, c))

            num += 1


def get_bridges():
    for isle, coordinates in isleDict.items():
        for row, col in coordinates:
            for i in range(4):
                que = deque([(row, col, 0)])
                while que:
                    r, c, l = que.popleft()
                    nr, nc = r + dr[i], c + dc[i]
                    if ((nr < 0 or nr >= n) or
                        (nc < 0 or nc >= m) or
                        maps[nr][nc] == isle):
                        continue
                    if maps[nr][nc] != 0:
                        if l > 1:
                            heapq.heappush(bridges, (l, isle, maps[nr][nc]))
                        break
                    que.append((nr, nc, l + 1))


def find(p):
    if isle[p] != p:
        isle[p] = find(isle[p])
    return isle[p]


def union(p, q):
    p, q = find(p), find(q)
    if p < q:
        isle[q] = p
    else:
        isle[p] = q


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for i in range(n)]
isleDict = defaultdict(set)
bridges = list()

dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)

get_islands()
get_bridges()

isle = [i for i in range(len(isleDict) + 1)]
result = 0

while bridges:
    dist, start, end = heapq.heappop(bridges)
    start, end = find(start), find(end)
    if start == end: continue
    union(start, end)
    result += dist

target = find(1)

for i in range(2, len(isleDict) + 1):
    if find(i) != target:
        print(-1)
        break
else:
    print(result)
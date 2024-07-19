from collections import deque
import heapq, sys

input = sys.stdin.readline


def find(p):
    if parent[p] == p:
        return p
    parent[p] = find(parent[p])
    return parent[p]


def union(p, q):
    p, q = find(p), find(q)
    if p == q:
        return False
    if p < q:
        parent[q] = p
    else:
        parent[p] = q
    return True


def get_dist(row, col):
    visited = [[False for j in range(n)] for k in range(n)]
    visited[row][col] = True
    que = deque([(row, col, 0)])
    cnt = 0

    while que:
        r, c, d = que.popleft()
        for j in range(4):
            nr, nc = r + dr[j], c + dc[j]
            if (
                nr < 0
                or nc < 0
                or nr >= n
                or nc >= n
                or visited[nr][nc]
                or maze[nr][nc] == "1"
            ):
                continue
            if maze[nr][nc] != "0":
                graph[key[(row, col)]][key[(nr, nc)]] = d + 1
                cnt += 1
            que.append((nr, nc, d + 1))
            visited[nr][nc] = True
            
    return cnt == m


def run():
    result = 0

    for r, c in key.keys():
        if not get_dist(r, c): return -1

    for i in range(m):
        for j in range(i + 1, m + 1):
            if graph[i][j] == int(1e9): continue
            heapq.heappush(heap, (graph[i][j], i, j))

    while heap:
        dist, i, j = heapq.heappop(heap)
        if union(i, j):
            result += dist

    for p in parent[1:]:
        p = find(p)
        if p != 0:
            return -1

    return result


dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

n, m = map(int, input().split())
parent = [i for i in range(m + 1)]
graph = [[int(1e9) for i in range(m + 1)] for j in range(m + 1)]
maze = list()
heap = list()
robot = None
key = dict()
idx = 1

for i in range(n):
    maze.append(input().rstrip())
    for j in range(n):
        if maze[i][j] == "S":
            key[(i, j)] = 0
            robot = [i, j]
        elif maze[i][j] == "K":
            key[(i, j)] = idx
            idx += 1

print(run())

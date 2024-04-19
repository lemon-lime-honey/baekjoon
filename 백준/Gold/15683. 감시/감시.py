from copy import deepcopy
import sys
input = sys.stdin.readline


def rotate(graph, idx):
    if idx == len(cams):
        global result
        result = min(result, cnt(graph))
        return

    new_map = deepcopy(graph)
    r, c = cams[idx]

    for nums in camera[graph[r][c]]:
        area(r, c, nums, new_map)
        rotate(new_map, idx + 1)
        new_map = deepcopy(graph)


def cnt(graph):
    res = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                res += 1

    return res


def area(r, c, nums, graph):
    for num in nums:
        nr, nc = r, c
        while True:
            nr += dr[num]
            nc += dc[num]
            if (nr < 0 or nr >= n or
                nc < 0 or nc >= m or
                graph[nr][nc] == 6):
                break
            if graph[nr][nc] == 0:
                graph[nr][nc] = 9


camera = [[],
          [[0], [1], [2], [3]],
          [[0, 2], [1, 3]],
          [[0, 1], [1, 2], [2, 3], [0, 3]],
          [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
          [[0, 1, 2, 3]]]

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

n, m = map(int, input().split())
result = int(1e9)
cams = list()
maps = list()

chk = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    maps.append(list(map(int, input().split())))
    for j in range(m):
        if maps[i][j] in range(1, 6):
            cams.append((i, j))

rotate(maps, 0)
print(result)
from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

n, l, r = map(int, input().split())
countries = [list(map(int, input().split())) for i in range(n)]
result = 0

while True:
    visited = [[False for i in range(n)] for j in range(n)]
    target = list()
    for i in range(n):
        for j in range(n):
            if visited[i][j]: continue
            visited[i][j] = True
            temp = [(i, j)]
            que = deque([(i, j)])
            while que:
                row, col = que.popleft()
                for k in range(4):
                    nr, nc = row + dr[k], col + dc[k]
                    if (0 <= nr < n) and (0 <= nc < n) and not visited[nr][nc]:
                        if l <= abs(countries[row][col] - countries[nr][nc]) <= r:
                            visited[nr][nc] = True
                            que.append((nr, nc))
                            temp.append((nr, nc))
            target.append(temp)
    if len(target) == n * n: break
    for country_set in target:
        if len(country_set) == 1: continue
        people = 0
        for row, col in country_set:
            people += countries[row][col]
        for row, col in country_set:
            countries[row][col] = people // len(country_set)
    result += 1

print(result)
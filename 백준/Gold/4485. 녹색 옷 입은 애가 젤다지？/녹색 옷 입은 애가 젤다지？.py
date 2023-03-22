from collections import deque
import sys
input = sys.stdin.readline

def dijkstra():
    rupee_lost = [[int(1e9) for i in range(n)] for j in range(n)]
    rupee_lost[0][0] = cave[0][0]
    que = deque([[0, 0]])

    while que:
        r, c = que.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if (0 <= nr < n) and (0 <= nc < n):
                if rupee_lost[r][c] + cave[nr][nc] < rupee_lost[nr][nc]:
                    rupee_lost[nr][nc] = rupee_lost[r][c] + cave[nr][nc]
                    que.append([nr, nc])
    
    return rupee_lost[n - 1][n - 1]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

ref = 1

while True:
    n = int(input())
    if not n:
        break

    cave = [list(map(int, input().split())) for i in range(n)]
    result = dijkstra()
    print(f'Problem {ref}: {result}')
    
    ref += 1
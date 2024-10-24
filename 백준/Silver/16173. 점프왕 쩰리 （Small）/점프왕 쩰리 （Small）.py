from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    que = deque([(0, 0)])

    while que:
        r, c = que.popleft()
        
        if maps[r][c] == 0:
            continue

        for i in range(2):
            nr, nc = r + dr[i] * maps[r][c] , c + dc[i] * maps[r][c]
            if nr >= n or nc >= n:
                continue
            if r == n - 1 and c == n - 1:
                return True

            que.append((nr, nc))

    return False


dr = [0, 1]
dc = [1, 0]

n = int(input())
maps = [list(map(int, input().split())) for i in range(n)]

print("HaruHaru" if bfs() else "Hing")

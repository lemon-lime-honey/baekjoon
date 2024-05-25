import sys
input = sys.stdin.readline


def chk():
    for i in range(1, n + 1):
        point = i
        for j in range(1, h + 1):
            if graph[j][point] == 1:
                point -= 1
            elif point < n and graph[j][point + 1] == 1:
                point += 1
        if point != i: return False
    return True


def backtrack(r, c, cnt):
    if chk():
        global answer
        answer = min(answer, cnt)
        return

    if cnt >= 3: return

    for i in range(r, h + 1):
        for j in range(n + 1):
            if graph[i][j] == 0 and graph[i][j - 1] == 0:
                if j < n and graph[i][j + 1] == 1: continue
                graph[i][j] = 1
                backtrack(i, j, cnt + 1)
                graph[i][j] = 0


n, m, h = map(int, input().split())
graph = [[0 for i in range(n + 1)] for j in range(h + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b + 1] = 1

answer = int(1e9)

backtrack(1, 1, 0)

print(-1 if answer == int(1e9) else answer)
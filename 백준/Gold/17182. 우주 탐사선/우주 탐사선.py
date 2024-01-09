import sys
input = sys.stdin.readline


def calc(point, total, cnt):
    if cnt == n:
        global result
        result = min(result, total)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            calc(i, total + time[point][i], cnt + 1)
            visited[i] = False


n, start = map(int, input().split())
time = [list(map(int, input().split())) for i in range(n)]
visited = [False for i in range(n)]
result = int(1e9)

for i in range(n):
    for j in range(n):
        for k in range(n):
            if time[j][i] + time[i][k] < time[j][k]:
                time[j][k] = time[j][i] + time[i][k]

calc(start, 0, 0)

print(result)
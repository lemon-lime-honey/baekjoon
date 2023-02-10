import sys

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    global cnt
    cnt += 1
    apt[x][y] = 2
    for i in range(4):
        del_x = x + dx[i]
        del_y = y + dy[i]
        if (0 <= del_x < n) and (0 <= del_y < n):
            if apt[del_x][del_y] == 1:
                dfs(del_x, del_y)

n = int(sys.stdin.readline())
apt = [[0 for i in range(n)] for j in range(n)]
result = list()

for i in range(n):
    apt[i] = list(map(int, sys.stdin.readline().strip()))

for i in range(n):
    for j in range(n):
        if apt[i][j] == 1:
            cnt = 0
            dfs(i, j)
            result.append(cnt)

result.sort()

print(len(result))
for element in result:
    print(element)

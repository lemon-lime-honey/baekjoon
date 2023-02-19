import sys

n = int(sys.stdin.readline())
triangle = [[] for i in range(n)]
result = list()
dr = [1, 1]
dc = [0, 1]

for i in range(n):
    triangle[i] = list(map(int, sys.stdin.readline().split()))
    result.append([0] * len(triangle[i]))

result[0][0] = triangle[0][0]

for i in range(n - 1):
    for j in range(len(triangle[i])):
        for k in range(2):
            nr = i + dr[k]
            nc = j + dc[k]
            temp = result[i][j] + triangle[nr][nc]
            if temp > result[nr][nc]:
                result[nr][nc] = temp

print(max(result[-1]))
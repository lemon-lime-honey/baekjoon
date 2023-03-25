import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
computer = [[INF for i in range(n)] for j in range(n)]
result = list()

for i in range(m):
    a, b, c = map(int, input().split())
    computer[a - 1][b - 1] = c
    computer[b - 1][a - 1] = c

for i in range(n):
    computer[i][i] = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if computer[j][i] + computer[i][k] < computer[j][k]:
                computer[j][k] = computer[j][i] + computer[i][k]

for i in range(n):
    result.append(sum(computer[i]) / n)

print(result.index(min(result)) + 1)
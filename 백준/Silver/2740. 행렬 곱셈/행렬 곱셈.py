import sys

n, m = map(int, sys.stdin.readline().split())
arrA = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    arrA[i] = list(map(int, sys.stdin.readline().split()))

m, k = map(int, sys.stdin.readline().split())
arrB = [[0 for i in range(k)] for j in range(m)]
for i in range(m):
    arrB[i] = list(map(int, sys.stdin.readline().split()))

result = [[0 for i in range(k)] for j in range(n)]
for i in range(n):
    for j in range(k):
        for l in range(m):
            result[i][j] += arrA[i][l] * arrB[l][j]

for i in range(n):
    print(*result[i])
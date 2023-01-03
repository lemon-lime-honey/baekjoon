import sys

n, m = map(int, sys.stdin.readline().strip().split())
result = []

for i in range(n):
    result.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(n):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(m):
        result[i][j] += temp[j]
    print(' '.join(map(str, result[i])))
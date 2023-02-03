import sys

n, m = map(int, sys.stdin.readline().split())
number = [[0 for i in range(m)]for j in range(n)]
add = [[0 for i in range(m)]for j in range(n)]

for i in range(n):
    number[i] = list(map(int, sys.stdin.readline().split()))

    if not i:
        for j in range(m):
            add[i][j] = number[i][j]
    else:
        for j in range(m):
            add[i][j] = add[i - 1][j] + number[i][j]

k = int(sys.stdin.readline())

for l in range(k):
    i, j, x, y = map(int, sys.stdin.readline().split())
    result = 0

    for o in range(j - 1, y):
        result += add[x - 1][o] - add[i - 1][o] + number[i - 1][o]
    
    print(result)
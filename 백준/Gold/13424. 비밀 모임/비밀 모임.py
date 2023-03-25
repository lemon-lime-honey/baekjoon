import sys
input = sys.stdin.readline
INF = sys.maxsize

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    way = [[INF for j in range(n)] for k in range(n)]

    for j in range(m):
        a, b, c = map(int, input().split())
        way[a - 1][b - 1] = c
        way[b - 1][a - 1] = c
    
    for j in range(n):
        way[j][j] = 0

    for j in range(n):
        for k in range(n):
            for l in range(n):
                if way[k][j] + way[j][l] < way[k][l]:
                    way[k][l] = way[k][j] + way[j][l]

    k = int(input())
    member = list(map(int, input().split()))
    result = [0 for j in range(n)]

    for j in range(k):
        for l in range(n):
            result[l] += way[member[j] - 1][l]

    print(result.index(min(result)) + 1)
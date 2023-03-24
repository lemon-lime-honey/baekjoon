import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
place = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if place[j][i] + place[i][k] < place[j][k]:
                place[j][k] = place[j][i] + place[i][k]

for i in range(m):
    a, b, c = map(int, input().split())
    if place[a - 1][b - 1] <= c:
        print('Enjoy other party')
    else:
        print('Stay here')
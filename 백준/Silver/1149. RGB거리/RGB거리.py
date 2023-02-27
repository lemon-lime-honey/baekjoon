import sys

n = int(sys.stdin.readline())
cost = list()
color = [[[[0 for i in range(3)] for j in range(3)] for k in range(3)] for l in range(n)]

for i in range(n):
    cost.append(list(map(int, sys.stdin.readline().split())))
    if not i:
        color[i] = cost[i]
    else:
        color[i][0] = min(color[i - 1][1], color[i - 1][2]) + cost[i][0]
        color[i][1] = min(color[i - 1][0], color[i - 1][2]) + cost[i][1]
        color[i][2] = min(color[i - 1][0], color[i - 1][1]) + cost[i][2]

print(min(color[-1]))
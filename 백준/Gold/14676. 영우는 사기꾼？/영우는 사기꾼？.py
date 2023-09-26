import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[] for i in range(n + 1)]
need = [list() for i in range(n + 1)]
building = [0 for i in range(n + 1)]
deg = [0 for i in range(n + 1)]
flag = True

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    need[y].append(x)
    deg[y] += 1

for i in range(k):
    a, b = map(int, input().split())
    if flag:
        if a == 1:
            if not deg[b]:
                for target in need[b]:
                    if building[target] == 0:
                        flag = False
                        break 
                else: building[b] += 1
            else: flag = False
        else:
            if building[b] == 0: flag = False
            else:
                if building[b] > 0:
                    building[b] -= 1
        for target in graph[b]:
            if deg[target] > 0:
                deg[target] -= 1

print('King-God-Emperor' if flag else 'Lier!')
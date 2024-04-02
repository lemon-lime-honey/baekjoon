from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    k, m, p = map(int, input().split())
    strahler = [0 for i in range(m + 1)]
    degree = [0 for i in range(m + 1)]
    river = [[] for i in range(m + 1)]
    data = [[] for i in range(m + 1)]
    order = list()
    que = deque()

    for j in range(p):
        a, b = map(int, input().split())
        river[b].append(a)
        data[a].append(b)
        degree[b] += 1

    for j in range(1, m + 1):
        if degree[j] == 0:
            que.append(j)
            order.append(j)
            strahler[j] = 1

    while que:
        point = que.popleft()
        for next_point in data[point]:
            degree[next_point] -= 1
            if degree[next_point] < 0: continue
            if degree[next_point] == 0:
                que.append(next_point)
                order.append(next_point)

    for point in order:
        if strahler[point] == 1: continue
        num, cnt = 0, 0
        for before in river[point]:
            if strahler[before] < num: continue
            elif strahler[before] == num: cnt += 1
            else: num, cnt = strahler[before], 1
        if cnt > 1:
            strahler[point] = num + 1
        else:
            strahler[point] = num

    print(k, strahler[m])
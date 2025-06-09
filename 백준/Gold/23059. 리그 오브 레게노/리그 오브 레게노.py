from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
item_map = dict()
idx_map = dict()
degree = list()
graph = list()
idx = 0

for i in range(n):
    a, b = input().split()
    if a not in item_map:
        item_map[a] = idx
        idx_map[idx] = a
        degree.append(0)
        graph.append(list())
        idx += 1
    if b not in item_map:
        item_map[b] = idx
        idx_map[idx] = b
        degree.append(0)
        graph.append(list())
        idx += 1
    degree[item_map[b]] += 1
    graph[item_map[a]].append(item_map[b])

result = list()
que = deque()

for i in range(idx):
    if degree[i] == 0:
        que.append(i)
        result.append(idx_map[i])

result.sort()

while que:
    length = len(que)
    temp = list()
    for i in range(length):
        now = que.popleft()
        for next_item in graph[now]:
            degree[next_item] -= 1
            if degree[next_item] == 0:
                que.append(next_item)
                temp.append(idx_map[next_item])
    if temp:
        temp.sort()
        result.extend(temp)

if len(result) == idx:
    print(*result, sep="\n")
else:
    print(-1)

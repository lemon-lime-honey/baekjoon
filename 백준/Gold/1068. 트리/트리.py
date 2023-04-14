def dfs(point):
    nodes[point] = -2
    for i in range(n):
        if point == nodes[i]:
            dfs(i)

n = int(input())
nodes = list(map(int, input().split()))
target = int(input())
result = 0

dfs(target)

for i in range(n):
    if nodes[i] != -2 and i not in nodes:
        result += 1

print(result)
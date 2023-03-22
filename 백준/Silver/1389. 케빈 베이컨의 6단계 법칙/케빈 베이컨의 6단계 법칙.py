import sys
input = sys.stdin.readline

n, m = map(int, input().split())
relation = [[int(1e9) for i in range(n + 1)] for j in range(n + 1)]
result = [0 for i in range(n + 1)]
smallest = int(1e9)
number = 0

for i in range(m):
    a, b = map(int, input().split())
    relation[a][b] = relation[b][a] = 1

for i in range(1, n + 1):
    relation[i][i] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            relation[j][k] = min(relation[j][k], relation[j][i] + relation[i][k])

for i in range(1, n + 1):
    result[i] = sum(relation[i][1:])
    if result[i] < smallest:
        number = i
        smallest = result[i]

print(number)
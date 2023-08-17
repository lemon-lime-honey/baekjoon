import sys
input = sys.stdin.readline

n = int(input())
graph = [[int(1e9) for i in range(58)] for j in range(58)]
result = set()

for i in range(n):
    ipt = list(input().rstrip())
    graph[ord(ipt[0]) - 65][ord(ipt[-1]) - 65] = 1

for i in range(58):
    graph[i][i] = 0

for i in range(58):
    for j in range(58):
        for k in range(58):
            if graph[j][k] > graph[j][i] + graph[i][k]:
                graph[j][k] = graph[j][i] + graph[i][k]

for i in range(58):
    for j in range(58):
        if i != j and graph[i][j] != int(1e9):
            result.add(f'{chr(i + 65)} => {chr(j + 65)}')

result = sorted(list(result))
print(len(result))
print(*result, sep='\n')
n, m = map(int, input().split())
graph = [[-1 for i in range(m)] for j in range(n)]
graph[0][0] = 1

for i in range(1, m):
    graph[0][i] = graph[0][i - 1]

for i in range(1, n):
    graph[i][0] = graph[i - 1][0] % 1000000007
    for j in range(1, m):
        graph[i][j] = (graph[i][j - 1] + graph[i - 1][j] + graph[i - 1][j - 1]) % 1000000007

print(graph[-1][-1])

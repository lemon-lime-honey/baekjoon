import sys
input = sys.stdin.readline

n = int(input())
graph = [[int(1e9) for i in range(26)] for j in range(26)]

for i in range(n):
    ipt = input().rstrip()
    graph[ord(ipt[0]) - ord('a')][ord(ipt[-1]) - ord('a')] = 1

for i in range(26):
    graph[i][i] = 0

for i in range(26):
    for j in range(26):
        for k in range(26):
            if graph[j][k] < graph[j][i] + graph[i][k]: continue
            graph[j][k] = graph[j][i] + graph[i][k]

m = int(input())

for i in range(m):
    ipt = input().rstrip()
    if graph[ord(ipt[0]) - ord('a')][ord(ipt[-1]) - ord('a')] == int(1e9):
        print('F')
    else:
        print('T')
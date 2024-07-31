import sys

input = sys.stdin.readline

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

t = int(input())

for i in range(t):
    ipt = input()
    r, c = map(int, input().split())
    graph = [input().rstrip() for j in range(r)]
    cnt = 0
    for j in range(r):
        for k in range(c):
            if (
                ord(graph[j][k]) == 118
                and j < r - 2
                and ord(graph[j + 1][k]) == 111
                and ord(graph[j + 2][k]) == 94
            ) or (
                ord(graph[j][k]) == 62
                and k < c - 2
                and ord(graph[j][k + 1]) == 111
                and ord(graph[j][k + 2]) == 60
            ):
                cnt += 1
    print(cnt)

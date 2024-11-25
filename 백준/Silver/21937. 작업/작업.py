import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

stack = [int(input())]
chk = set()

while stack:
    work = stack.pop()

    for next_work in graph[work]:
        if next_work not in chk:
            stack.append(next_work)
            chk.add(next_work)

print(len(chk))
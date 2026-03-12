import sys

input = sys.stdin.readline

n, m = map(int, input().split())

room = [0 for i in range(n + 1)]
result = list()

for i in range(m):
    k, s, e = map(int, input().split())
    if s >= room[k]:
        room[k] = e
        result.append("YES")
    else:
        result.append("NO")

print(*result, sep="\n")

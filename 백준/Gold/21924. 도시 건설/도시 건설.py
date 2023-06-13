import sys
input = sys.stdin.readline


def find(p):
    if p != buildings[p]:
        buildings[p] = find(buildings[p])
    return buildings[p]


def union(p1, p2):
    p1, p2 = find(p1), find(p2)
    if p1 == p2: return
    if p1 < p2: buildings[p2] = p1
    else: buildings[p1] = p2


n, m = map(int, input().split())
data = [list(map(int, input().split())) for i in range(m)]
buildings = [i for i in range(n + 1)]
original = 0
data.sort(key=lambda x:x[2])
result = 0

for start, end, cost in data:
    original += cost
    if find(start) != find(end):
        union(start, end)
        result += cost

ref = find(buildings[1])

for i in range(2, n + 1):
    chk = find(i)
    if ref != chk:
        print(-1)
        sys.exit()

print(original - result)
import sys
input = sys.stdin.readline


def find(p):
    if p != chk[p]:
        chk[p] = find(chk[p])
    return chk[p]


def union(p1, p2):
    p1, p2 = find(p1), find(p2)
    if p1 == p2: return
    if p1 < p2: chk[p2] = p1
    else: chk[p1] = p2


n, m = map(int, input().split())
chk = [i for i in range(n + 1)]
road = [list(map(int, input().split())) for i in range(m)]
road.sort(key=lambda x:x[2])
result = 0
maximum = 0

for a, b, c in road:
    if find(a) != find(b):
        maximum = max(maximum, c)
        union(a, b)
        result += c

result -= maximum
print(result)
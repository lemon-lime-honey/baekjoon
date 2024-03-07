import sys
input = sys.stdin.readline


def find(p):
    if ally[p] != p:
        ally[p] = find(ally[p])
    return ally[p]


def union(p, q):
    p, q = find(p), find(q)
    if p < q: ally[q] = p
    else: ally[p] = q


n, m = map(int, input().split())
ally = [i for i in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    union(x, y)

c, h, k = map(int, input().split())
allydict = dict()
c = find(c)
h = find(h)

for i in range(1, n + 1):
    target = find(i)
    allydict[target] = allydict.get(target, 0) + 1

kingdoms = sorted(allydict.items(), key=lambda x: -x[1])
result = allydict[c]
cnt = 0

for key, value in kingdoms:
    if cnt == k: break
    if find(key) in (c, h): continue
    result += value
    cnt += 1

print(result)
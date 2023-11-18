import sys
input = sys.stdin.readline


def find(p):
    if relation[p] != p:
        relation[p] = find(relation[p])
    return relation[p]


def union(p, q):
    p, q = find(p), find(q)
    if p == q: return
    if p < q: relation[q] = p
    else: relation[p] = q


n, m = map(int, input().split())
enemy = [i for i in range(n + 1)]
relation = [i for i in range(n + 1)]
result = True

for i in range(m):
    a, b = map(int, input().split())
    if not result: continue
    if find(a) == find(b):
        result = False
    else:
        if enemy[a] == a:
            enemy[a] = b
        else:
            union(b, enemy[a])
        if enemy[b] == b:
            enemy[b] = a
        else:
            union(a, enemy[b])

print(1 if result else 0)
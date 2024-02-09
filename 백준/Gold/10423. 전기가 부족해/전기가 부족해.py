import sys
input = sys.stdin.readline


def find(p):
    if city[p] != p:
        city[p] = find(city[p])
    return city[p]


def union(p, q):
    p, q = find(p), find(q)

    if p < q:
        city[q] = p
    else:
        city[p] = q


n, m, k = map(int, input().split())
plants = list(map(int, input().split()))
city = [i for i in range(n + 1)]

for plant in plants:
    city[plant] = 0

cables = sorted([list(map(int, input().split())) for i in range(m)], key=lambda x: x[2])
result = 0

for i in range(m):
    start, end, cost = cables[i]
    if (find(start) != find(end)):
        result += cost
        union(start, end)
        for j in range(1, n + 1):
            if city[j] != 0:
                break
        else:
            break

print(result)
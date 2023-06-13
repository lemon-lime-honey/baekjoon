import sys
input = sys.stdin.readline


def find(p):
    if p != house[p]:
        house[p] = find(house[p])
    return house[p]


def union(p1, p2):
    p1, p2 = find(p1), find(p2)
    if p1 == p2: return
    if p1 < p2: house[p2] = p1
    else: house[p1] = p2


while True:
    m, n = map(int, input().split())
    if m == n == 0: break

    routes = list()
    house = [i for i in range(m)]
    result = 0

    for i in range(n):
        x, y, z = map(int, input().split())
        routes.append((z, x, y))

    routes.sort()

    for cost, start, end in routes:
        if find(start) != find(end): union(start, end)
        else:
            result += cost

    print(result)
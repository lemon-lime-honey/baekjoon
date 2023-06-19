import sys
input = sys.stdin.readline


def find(p):
    if p != planes[p]:
        planes[p] = find(planes[p])
    return planes[p]


def union(p1, p2):
    p1, p2 = find(p1), find(p2)
    if p1 == p2: return True
    if p1 < p2: planes[p2] = p1
    else: planes[p1] = p2
    return False


t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    planes = [i for i in range(n + 1)]
    result = 0

    for j in range(m):
        a, b = map(int, input().split())
        chk = union(a, b)
        if not chk: result += 1

    print(result)
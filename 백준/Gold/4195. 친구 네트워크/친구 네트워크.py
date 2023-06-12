import sys
input = sys.stdin.readline


def find(p):
    if p != root[p]:
        root[p] = find(root[p])
    return root[p]


def union(p1, p2):
    p1, p2 = find(p1), find(p2)
    if p1 == p2: return friend[p1]
    root[p2] = p1
    friend[p1] += friend[p2]
    return friend[p1]

t = int(input())

for i in range(t):
    f = int(input())
    root = dict()
    friend = dict()

    for j in range(f):
        a, b = map(str, input().strip().split())

        if root.get(a) is None:
            root[a] = a
            friend[a] = 1
        if root.get(b) is None:
            root[b] = b
            friend[b] = 1

        result = union(a, b)
        print(result)
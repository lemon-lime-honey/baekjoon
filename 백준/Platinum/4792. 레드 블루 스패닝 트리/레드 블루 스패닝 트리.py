import heapq, sys

input = sys.stdin.readline


def find(p, parent):
    if p != parent[p]:
        parent[p] = find(parent[p], parent)
    return parent[p]


def union(p, q, parent):
    p, q = find(p, parent), find(q, parent)
    if p == q:
        return False
    if p < q:
        parent[q] = p
    else:
        parent[p] = q
    return True


result = list()

while True:
    n, m, k = map(int, input().split())
    if n == m == k:
        break

    smallest = [i for i in range(n + 1)]
    largest = [i for i in range(n + 1)]
    s_que = list()
    l_que = list()
    res = [0, 0]

    for i in range(m):
        ipt = input().split()
        f, t = int(ipt[1]), int(ipt[2])
        if ipt[0] == "R":
            heapq.heappush(s_que, (0, f, t))
            heapq.heappush(l_que, (1, f, t))
        else:
            heapq.heappush(s_que, (1, f, t))
            heapq.heappush(l_que, (0, f, t))

    while s_que:
        c, f, t = heapq.heappop(s_que)
        if union(f, t, smallest) and c == 1:
            res[0] += 1

    while l_que:
        c, f, t = heapq.heappop(l_que)
        if union(f, t, largest) and c == 0:
            res[1] += 1

    if res[0] <= k <= res[1]:
        result.append(1)
    else:
        result.append(0)

print(*result, sep="\n")

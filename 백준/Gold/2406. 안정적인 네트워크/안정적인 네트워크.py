import heapq, sys

input = sys.stdin.readline


def find(p: int) -> int:
    if p != connected[p]:
        connected[p] = find(connected[p])
    return connected[p]


def union(p: int, q: int) -> bool:
    p, q = find(p), find(q)
    if p == q:
        return False
    if p < q:
        connected[q] = p
    else:
        connected[p] = q
    return True


if __name__ == "__main__":
    n, m = map(int, input().split())
    connected = [i for i in range(n)]
    result = list()
    total_cost = 0

    for i in range(m):
        u, v = map(int, input().split())
        union(u - 1, v - 1)

    cost = list()

    for i in range(n):
        ipt = list(map(int, input().split()))
        for j in range(n):
            if ipt[j] == 0:
                continue
            heapq.heappush(cost, (ipt[j], i, j))

    while cost:
        c, u, v = heapq.heappop(cost)
        if u == 0 or v == 0:
            continue
        if not union(u, v):
            continue
        result.append((u, v))
        total_cost += c

    print(total_cost, len(result))

    for u, v in result:
        print(u + 1, v + 1)

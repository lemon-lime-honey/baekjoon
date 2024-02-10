from collections import defaultdict
import heapq, sys
input = sys.stdin.readline


def prim(flag):
    chk = set()
    heap = [(0, 0)]
    result = 0

    while len(chk) < n + 1:
        up, point = heapq.heappop(heap)
        if point in chk: continue
        result += flag * up
        chk.add(point)

        for next_point, next_up in routes[point]:
            if next_point in chk: continue
            heapq.heappush(heap, (flag * next_up, next_point))

    return result


n, m = map(int, input().split())
routes = defaultdict(list)

for i in range(m + 1):
    a, b, c = map(int, input().split())
    if c == 0: c = 1
    else: c = 0
    routes[a].append((b, c))
    routes[b].append((a, c))

most = prim(-1)
least = prim(1)

print(most * most - least * least)
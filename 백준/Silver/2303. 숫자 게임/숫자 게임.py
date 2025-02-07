from itertools import combinations
import heapq, sys

input = sys.stdin.readline

n = int(input())
heap = list()

for i in range(1, n + 1):
    cards = list(map(int, input().split()))
    combs = combinations(cards, 3)
    res = 0

    for comb in combs:
        res = max(res, sum(comb) % 10)

    heapq.heappush(heap, (-res, -i))

print(-heap[0][1])

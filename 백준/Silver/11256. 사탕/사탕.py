import heapq

t = int(input())
result = list()

for i in range(t):
    j, n = map(int, input().split())
    box = list()
    candy = 0
    res = 0

    for k in range(n):
        r, c = map(int, input().split())
        heapq.heappush(box, (-1 * r * c))

    while candy < j:
        candy -= heapq.heappop(box)
        res += 1

    result.append(res)

print(*result, sep="\n")

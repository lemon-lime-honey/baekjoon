import heapq, sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
cost = list()
result = 0

for i in range(n):
    p, q = map(int, input().split())
    heapq.heappush(cost, (-abs(p - q), p, q))

while cost:
    diff, p, q = heapq.heappop(cost)
    if p < q:
        if a > 0:
            a -= 1
            result += p
        else:
            b -= 1
            result += q
    elif q < p:
        if b > 0:
            b -= 1
            result += q
        else:
            a -= 1
            result += p
    else:
        result += p

print(result)

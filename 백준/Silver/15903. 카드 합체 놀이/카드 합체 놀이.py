import heapq

n, m = map(int, input().split())
cards = list(map(int, input().split()))

heapq.heapify(cards)

for i in range(m):
    one, two = heapq.heappop(cards), heapq.heappop(cards)
    one, two = one + two, one + two
    heapq.heappush(cards, one)
    heapq.heappush(cards, two)

print(sum(cards))
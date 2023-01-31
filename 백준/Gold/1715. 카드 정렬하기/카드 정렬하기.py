import heapq, sys

n = int(sys.stdin.readline())
card = list()
temp = 0
result = 0

for i in range(n):
    heapq.heappush(card, int(sys.stdin.readline()))

while len(card) > 1:
    temp =  heapq.heappop(card) + heapq.heappop(card)
    result += temp
    heapq.heappush(card, temp)

print(result)
import heapq

n = int(input())
data = list()

for i in range(n):
    s, c, l = map(int, input().split())
    heapq.heappush(data, (-s, c, l, i + 1))

print(data[0][-1])

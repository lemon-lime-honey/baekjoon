import heapq

ipt = input()
result = list()

for i in range(len(ipt)):
    heapq.heappush(result, ipt[i:])

while result:
    print(heapq.heappop(result))
import heapq

n = int(input())
plusHeap = list()
minusHeap = list()

for i in range(n):
    temp = int(input())
    if temp > 0:
        heapq.heappush(plusHeap, -1 * temp)
    else:
        heapq.heappush(minusHeap, temp)

total = 0
before = int(1e9)

while plusHeap:
    temp = -1 * heapq.heappop(plusHeap)
    if before == int(1e9):
        before = temp
    else:
        if temp * before > temp + before:
            total += temp * before
        else:
            total += temp + before
        before = int(1e9)
    
if before != int(1e9):
    total += before
    before = int(1e9)

while minusHeap:
    temp = heapq.heappop(minusHeap)
    if before == int(1e9):
        before = temp
    else:
        if temp * before > temp + before:
            total += temp * before
        else:
            total += temp + before
        before = int(1e9)
    
if before != int(1e9):
    total += before

print(total)
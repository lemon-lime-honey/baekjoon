import heapq

w = list()
k = list()
scoreW = 0
scoreK = 0

for i in range(20):
    if i <10:
        heapq.heappush(w, -1 * int(input()))
    else:
        heapq.heappush(k, -1 * int(input()))

for i in range(3):
    scoreW += -1 * heapq.heappop(w)
    scoreK += -1 * heapq.heappop(k)

print(f'{scoreW} {scoreK}')
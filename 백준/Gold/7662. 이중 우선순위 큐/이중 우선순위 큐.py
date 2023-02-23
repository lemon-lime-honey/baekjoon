import heapq, sys

t = int(sys.stdin.readline())

for i in range(t):
    k = int(sys.stdin.readline())
    maxHeap = list()
    minHeap = list()
    chk = [True] * k
    
    for j in range(k):
        command = list(sys.stdin.readline().split())
        if command[0] == 'I':
            heapq.heappush(maxHeap, (-1 * int(command[1]), j))
            heapq.heappush(minHeap, (int(command[1]), j))
        if command[0] == 'D':
            if len(maxHeap) or len(minHeap):
                if int(command[1]) == 1:
                    while maxHeap and not chk[maxHeap[0][1]]:
                        heapq.heappop(maxHeap)
                    if maxHeap:
                        chk[maxHeap[0][1]] = False
                        heapq.heappop(maxHeap)
                elif int(command[1]) == -1:
                    while minHeap and not chk[minHeap[0][1]]:
                        heapq.heappop(minHeap)
                    if minHeap:
                        chk[minHeap[0][1]] = False
                        heapq.heappop(minHeap)
    
    while maxHeap and not chk[maxHeap[0][1]]:
        heapq.heappop(maxHeap)
    while minHeap and not chk[minHeap[0][1]]:
        heapq.heappop(minHeap)
    
    if maxHeap and minHeap:
        print(-1 * maxHeap[0][0], minHeap[0][0])
    else:
        print('EMPTY')
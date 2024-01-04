import heapq, sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    k = int(input())
    chapters = list(map(int, input().split()))
    heapq.heapify(chapters)
    result = 0

    while len(chapters) > 1:
        temp = heapq.heappop(chapters) + heapq.heappop(chapters)
        result += temp
        heapq.heappush(chapters, temp)

    print(result)
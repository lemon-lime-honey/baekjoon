import heapq, sys
input = sys.stdin.readline

n, h, t = map(int, input().split())
heights = list()
result = 0

for i in range(n):
    heapq.heappush(heights, -int(input()))

while result < t:
    target = -heapq.heappop(heights)
    if target < h: break
    if target == 1:
        heapq.heappush(heights, -1)
    else:
        heapq.heappush(heights, -(target // 2))
    result += 1

if result < t or -heights[0] < h:
    print('YES', result, sep='\n')
else:
    print('NO', -heights[0], sep='\n')

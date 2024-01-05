import heapq, sys
input = sys.stdin.readline

n = int(input())
works = list()
cups = list()
time = 0

for i in range(n):
    a, b = map(int, input().split())
    works.append((a, b))

works.sort(key=lambda x: (x[0], -x[1]))

for i in range(n):
    heapq.heappush(cups, works[i][1])
    if works[i][0] < len(cups):
        heapq.heappop(cups)

print(sum(cups))
import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
bus = [[] for i in range(n + 1)]
result = [int(1e9)] * (n + 1)

for i in range(m):
    start, end, cost = map(int, input().split())
    heapq.heappush(bus[start], (cost, end))

initial, final = map(int, input().split())
que = [(0, initial)]

while que:
    length, point = heapq.heappop(que)

    while bus[point]:
        next_length, next_point = heapq.heappop(bus[point])
        if length + next_length < result[next_point]:
            heapq.heappush(que, (length + next_length, next_point))
            result[next_point] = length + next_length

print(result[final])
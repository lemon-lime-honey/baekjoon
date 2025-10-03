import heapq

n = int(input())
data = list()
time = 0

for i in range(n):
    heapq.heappush(data, list(map(int, input().split())))

while data:
    start, duration = heapq.heappop(data)
    if time <= start:
        time = start + duration
    else:
        time += duration

print(time)

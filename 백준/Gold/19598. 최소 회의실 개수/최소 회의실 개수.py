import heapq, sys
input = sys.stdin.readline

n = int(input())
schedule = list()
room = [0]

for i in range(n):
    heapq.heappush(schedule, list(map(int, input().split())))

while schedule:
    start, end = heapq.heappop(schedule)
    if room[0] <= start:
        heapq.heappop(room)
    heapq.heappush(room, end)

print(len(room))
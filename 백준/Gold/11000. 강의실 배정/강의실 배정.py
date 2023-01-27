import heapq, sys

n = int(sys.stdin.readline())
lecture = list()
room = [1]

for i in range(n):
    n1, n2 = map(int, sys.stdin.readline().split())
    heapq.heappush(lecture, (n1, n2))

while lecture:
    time = heapq.heappop(lecture)
    ref = heapq.heappop(room)
    if ref <= time[0]:
        ref = time[1]
        heapq.heappush(room, ref)
    else:
        heapq.heappush(room, ref)
        heapq.heappush(room, time[1])

print(len(room))
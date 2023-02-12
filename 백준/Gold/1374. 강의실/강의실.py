import heapq, sys

lecture_num = int(sys.stdin.readline())
lecture = list()
room = [(0, 0)]

for i in range(lecture_num):
    number, start, end = map(int, sys.stdin.readline().split())
    heapq.heappush(lecture, (start, end))

while lecture:
    time = heapq.heappop(lecture)
    space = heapq.heappop(room)
    if space[0] <= time[0]:
        heapq.heappush(room, (time[1], time[0]))
    else:
        heapq.heappush(room, space)
        heapq.heappush(room, (time[1], time[0]))

print(len(room))
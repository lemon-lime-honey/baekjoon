import heapq

seminar = list()

for i in range(7):
    name, number = input().split()
    heapq.heappush(seminar, (-int(number), name))

print(seminar[0][1])

import heapq, sys
input = sys.stdin.readline

n = int(input())
data = list()
maxDay = 0
result = 0
time = 0

for i in range(n):
    p, d = map(int, input().split())
    heapq.heappush(data, (-p, d))
    maxDay = max(maxDay, d)

days = [False for i in range(maxDay + 1)]

while data:
    pay, day = heapq.heappop(data)

    while days[day] and day > 1:
        day -= 1

    if not days[day]:
        days[day] = True
        result -= pay

print(result)
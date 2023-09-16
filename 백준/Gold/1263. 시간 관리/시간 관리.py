import heapq, sys
input = sys.stdin.readline

n = int(input())
task = list()
time = int(1e12)

for i in range(n):
    t, s = map(int, input().split())
    heapq.heappush(task, (-s, t))

while task:
    s, t = heapq.heappop(task)
    s = -s

    if time == int(1e9):
        time = s - t
    else:
        if time > s: time = s - t
        else: time -= t

print(time if time >= 0 else -1)
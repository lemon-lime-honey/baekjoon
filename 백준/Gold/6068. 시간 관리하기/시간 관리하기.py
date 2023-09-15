import heapq, sys
input = sys.stdin.readline

n = int(input())
result = list()
data = list()
time = 0

for i in range(n):
    t, s = map(int, input().split())
    heapq.heappush(data, (-s, t))

while data:
    s, t = heapq.heappop(data)
    s = -s
    if not time:
        time = s - t
    else:
        if time > s:
            time = s - t
        else:
            time -= t

print(time if time >= 0 else -1)
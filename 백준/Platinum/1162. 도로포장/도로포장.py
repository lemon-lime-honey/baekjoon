import heapq, sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
roads = [[] for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    roads[a].append((b, c))
    roads[b].append((a, c))

chk = [[float('inf') for i in range(k + 1)] for j in range(n + 1)]
que = [(0, 0, 1)]
chk[1][0] = 0

while que:
    time, cnt, point = heapq.heappop(que)
    if chk[point][cnt] < time: continue
    for next_point, next_time in roads[point]:
        if cnt < k and chk[next_point][cnt + 1] > time:
            chk[next_point][cnt + 1] = time
            heapq.heappush(que, (time, cnt + 1, next_point))
        if chk[next_point][cnt] <= time + next_time:
            continue
        chk[next_point][cnt] = time + next_time
        heapq.heappush(que, (time + next_time, cnt, next_point))

print(min(chk[n]))
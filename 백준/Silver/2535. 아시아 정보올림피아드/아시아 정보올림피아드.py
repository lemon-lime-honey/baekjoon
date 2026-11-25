import heapq

n = int(input())
cnt = [[] for i in range(101)]
total = []

for i in range(n):
    country, idx, score = map(int, input().split())
    heapq.heappush(cnt[country], (-score, idx))

for i in range(1, 101):
    for j in range(2):
        if not cnt[i]:
            break
        score, idx = heapq.heappop(cnt[i])
        heapq.heappush(total, (score, i, idx))

for i in range(3):
    print(total[0][1], total[0][2])
    heapq.heappop(total)

import heapq

k, n = map(int, input().split())
nums = list(map(int, input().split()))
hq = list()

for num in nums:
    heapq.heappush(hq, num)

for i in range(n):
    chk = heapq.heappop(hq)
    for num in nums:
        calc = chk * num
        heapq.heappush(hq, calc)
        if chk % num == 0:
            break

print(chk)

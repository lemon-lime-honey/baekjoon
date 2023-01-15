import heapq
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

heapA = list()
heapB = list()
ref = list()
result = 0

for i in range(n):
    heapq.heappush(heapA, (a[i], i))
    heapq.heappush(heapB, (-1 * b[i], i))

for i in range(n):
    ref.append(heapq.heappop(heapA)[1])

for i in range(n):
    result += a[ref[i]] * -1 * heapq.heappop(heapB)[0]

print(result)
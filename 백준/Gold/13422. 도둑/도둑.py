import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m, k = map(int, input().split())
    village = list(map(int, input().split()))
    start, end = 0, m - 1
    total = 0
    cnt = 0

    for j in range(start, end + 1): total += village[j]

    if total < k: cnt += 1
    start += 1
    end += 1

    if end >= n:
        print(cnt)
        continue

    while True:
        total = total - village[start - 1] + village[end]
        if total < k: cnt += 1
        start += 1
        end += 1
        if end >= n: end = 0
        if start >= n: break

    print(cnt)
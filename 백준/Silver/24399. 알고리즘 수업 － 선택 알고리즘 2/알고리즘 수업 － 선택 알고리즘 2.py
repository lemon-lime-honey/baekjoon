import sys
sys.setrecursionlimit(10**4)


def select(p, r, k):
    if k > 0 and k <= r - p + 1:
        i = partition(p, r)
        if i - p == k - 1:
            return arr[i]
        if i - p > k - 1:
            return select(p, i - 1, k)
        return select(i + 1, r, k - i + p - 1)


def partition(p, r):
    global cnt, result
    x = arr[r]
    i = p
    for j in range(p, r):
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            cnt += 1
            if cnt == K:
                result = list(arr)
    arr[i], arr[r] = arr[r], arr[i]
    cnt += 1
    if cnt == K:
        result = list(arr)
    return i
    

N, Q, K = map(int, input().split())
arr = list(map(int, input().split()))
result = None
cnt = 0

select(0, N - 1, Q)
if result: print(*result)
else: print(-1)

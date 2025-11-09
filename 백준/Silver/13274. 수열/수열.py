n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

for i in range(k):
    l, r, x = map(int, input().split())
    for j in range(l - 1, r):
        arr[j] += x
    arr.sort()

print(*arr)

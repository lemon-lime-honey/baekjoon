from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
idx = dict()
arr = list()

for i in range(n):
    idx[a[i]] = i

for i in range(n):
    arr.append(idx[b[i]])

result = [arr[0]]

for i in range(1, n):
    if result[-1] < arr[i]:
        result.append(arr[i])
    else:
        target = bisect_left(result, arr[i])
        result[target] = arr[i]

print(len(result))
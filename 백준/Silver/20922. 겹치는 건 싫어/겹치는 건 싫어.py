n, k = map(int, input().split())
a = list(map(int, input().split()))
numDict = dict()

lo, hi = 0, 1
result = 1
numDict[a[lo]] = 1

while hi < n:
    if a[hi] not in numDict:
        numDict[a[hi]] = 1
        hi += 1
    elif numDict[a[hi]] < k:
        numDict[a[hi]] += 1
        hi += 1
    else:
        while a[lo] != a[hi]:
            numDict[a[lo]] -= 1
            lo += 1
        lo += 1
        hi += 1
    result = max(result, hi - lo)

print(result)
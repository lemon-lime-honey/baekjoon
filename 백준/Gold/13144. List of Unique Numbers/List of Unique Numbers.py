n = int(input())
array = list(map(int, input().split()))
lo, hi, cnt = 0, 1, 1
seen = {array[0]}

while lo <= hi and hi < n:
    if array[hi] in seen:
        while array[hi] in seen:
            seen.discard(array[lo])
            lo += 1
    else:
        seen.add(array[hi])
        hi += 1
        cnt += hi - lo

print(cnt)
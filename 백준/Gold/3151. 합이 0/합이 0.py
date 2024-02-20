from bisect import bisect_left

n = int(input())
a = sorted(list(map(int, input().split())))
result = 0

for i in range(n):
    lo, hi = i + 1, n - 1
    while lo < hi:
        chk = a[i] + a[lo] + a[hi]
        if chk > 0:
            hi -= 1
        elif chk < 0:
            lo += 1
        else:
            if a[lo] == a[hi]:
                result += hi - lo
            else:
                result += hi - bisect_left(a, a[hi]) + 1
            lo += 1

print(result)
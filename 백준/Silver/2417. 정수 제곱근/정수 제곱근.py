from sys import exit

n = int(input())

if n < 2: print(n)
else:
    lo, hi = 1, n

    while lo <= hi:
        mid = (lo + hi) // 2
        chk = mid * mid
        if chk == n:
            print(mid)
            exit()
        if chk < n: lo = mid + 1
        else: hi = mid - 1

    print(lo)
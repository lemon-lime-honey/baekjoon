import sys
input = sys.stdin.readline


def bin_search(target, end):
    lo, hi = 0, n - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if target < dots[mid]:
            hi = mid - 1
        elif target > dots[mid]:
            lo = mid + 1
        else:
            return mid
    
    if end: return hi
    return lo


n, m = map(int, input().split())
dots = sorted(list(map(int, input().split())))

for i in range(m):
    start, end = map(int, input().split())
    initial, last = bin_search(start, False), bin_search(end, True)
    print(last - initial + 1)
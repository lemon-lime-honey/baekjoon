import sys
input = sys.stdin.readline

n = int(input())
soldiers = list(map(int, input().split()))
result = [10000001]

for i in range(n):
    if result[-1] > soldiers[i]:
        result.append(soldiers[i])
    else:
        lo, hi = 1, len(result) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if result[mid] < soldiers[i]:
                hi = mid
            else:
                lo = mid + 1
        result[hi] = soldiers[i]

print(n - (len(result) - 1))
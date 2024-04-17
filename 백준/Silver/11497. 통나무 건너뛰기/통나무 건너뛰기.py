import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    l = sorted(list(map(int, input().split())))
    result = [0 for i in range(n)]
    lo, hi = 0, n - 1
    
    for i in range(n):
        if i % 2 == 0:
            result[lo] = l[i]
            lo += 1
        else:
            result[hi] = l[i]
            hi -= 1

    gap = abs(result[-1] - result[0])

    for i in range(1, n):
        gap = max(gap, abs(result[i] - result[i - 1]))

    print(gap)
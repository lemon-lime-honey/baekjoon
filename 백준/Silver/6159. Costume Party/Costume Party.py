import sys
input = sys.stdin.readline

n, s = map(int, input().split())
cows = sorted([int(input()) for i in range(n)])
result, hi = 0, n - 1

for lo in range(n - 1):
    while cows[lo] + cows[hi] > s and lo < hi:
        hi -= 1
    result += hi - lo
    hi = n - 1

print(result)
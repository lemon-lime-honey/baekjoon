import sys
input = sys.stdin.readline

h, w = map(int, input().split())
heights = list(map(int, input().split()))

lo, hi = 0, w - 1
maxL, maxR = heights[0], heights[-1]
result = 0

while lo < hi:
    if maxL < maxR:
        lo += 1
        maxL = max(maxL, heights[lo])
        result += max(0, maxL - heights[lo])
    else:
        hi -= 1
        maxR = max(maxR, heights[hi])
        result += max(0, maxR - heights[hi])

print(result)
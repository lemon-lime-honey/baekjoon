import sys
input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))
lo, hi = 0, n - 1
result = liquid[lo] + liquid[hi]
res = [0, n - 1]

while lo < hi:
    temp = liquid[lo] + liquid[hi]
    if abs(temp) < abs(result):
        result = temp
        res = lo, hi
        if not result: break
    if temp < 0:
        lo += 1
    else:
        hi -= 1

print(liquid[res[0]], liquid[res[1]])
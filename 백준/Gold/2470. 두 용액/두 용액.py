n = int(input())
liquid = sorted(list(map(int, input().split())))
lo, hi = 0, n - 1
result = [liquid[0], liquid[-1]]

while lo < hi:
    temp = liquid[lo] + liquid[hi]
    if abs(temp) < abs(result[0] + result[1]):
        result = liquid[lo], liquid[hi]
    if temp < 0: lo += 1
    else: hi -= 1

print(*result)
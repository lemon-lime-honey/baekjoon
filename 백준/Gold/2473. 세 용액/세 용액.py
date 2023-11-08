import sys
input = sys.stdin.readline

n = int(input())
liquid = sorted(list(map(int, input().split())))
result = [int(1e10), 0, 0, 0]

for i in range(n):
    lo, hi = i + 1, n - 1

    while lo < hi:
        chk = liquid[i] + liquid[lo] + liquid[hi]
        if abs(chk) < result[0]:
            result = [abs(chk), i, lo, hi]
            if chk < 0:
                lo += 1
            else: hi -= 1
        elif chk < 0: lo += 1
        else: hi -= 1

    
print(liquid[result[1]], liquid[result[2]], liquid[result[3]])
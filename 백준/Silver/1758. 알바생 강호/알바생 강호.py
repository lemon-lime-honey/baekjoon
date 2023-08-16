import sys
input = sys.stdin.readline

n = int(input())
tips = [int(input()) for i in range(n)]
desc = sorted(tips, reverse=True)
asc = sorted(tips)
r1 = 0
r2 = 0

for i in range(n):
    if asc[i] - i > 0:
        r1 += asc[i] - i
    if desc[i] - i > 0:
        r2 += desc[i] - i

print(max(r1, r2))
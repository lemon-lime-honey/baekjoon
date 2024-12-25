import sys

input = sys.stdin.readline

n = int(input())
original_hole = list(map(int, input().split()))
q = int(input())
acorn = list(map(int, input().split()))
hole = [0 for i in range(n)]

before = 0

for i in range(n):
    if before < original_hole[i] + i:
        before = original_hole[i] + i
    hole[i] = before

result = list()

for a in acorn:
    lo, hi = 0, n - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if a <= hole[mid]:
            hi = mid
        else:
            lo = mid + 1
    result.append(lo + 1)

print(*result)

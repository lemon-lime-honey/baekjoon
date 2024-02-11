import sys, bisect
input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

prefix_a = list()
prefix_b = list()

for i in range(n):
    target = a[i]
    prefix_a.append(target)
    for j in range(i + 1, n):
        target += a[j]
        prefix_a.append(target)

for i in range(m):
    target = b[i]
    prefix_b.append(target)
    for j in range(i + 1, m):
        target += b[j]
        prefix_b.append(target)

prefix_b.sort()
result = 0

for i in range(len(prefix_a)):
    chk = t - prefix_a[i]
    lo = bisect.bisect_left(prefix_b, chk)
    hi = bisect.bisect_right(prefix_b, chk)
    result += hi - lo

print(result)
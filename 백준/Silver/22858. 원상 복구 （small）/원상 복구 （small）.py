import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().split()))
d = list(map(int, input().split()))

for i in range(k):
    temp = [0 for i in range(n)]
    for j in range(n):
        temp[d[j] - 1] = s[j]
    s = temp

print(*s)
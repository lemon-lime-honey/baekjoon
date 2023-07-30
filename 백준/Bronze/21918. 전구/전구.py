import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lamp = list(map(int, input().split()))

for i in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        lamp[b - 1] = c
    elif a == 2:
        for j in range(b - 1, c):
            lamp[j] = 0 if lamp[j] else 1
    elif a == 3:
        for j in range(b - 1, c):
            lamp[j] = 0
    elif a == 4:
        for j in range(b - 1, c):
            lamp[j] = 1

print(*lamp)
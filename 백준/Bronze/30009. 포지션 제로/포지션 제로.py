n = int(input())
x, y, r = map(int, input().split())
lines = [int(input()) for i in range(n)]

a, b = 0, 0

for line in lines:
    if x - r < line < x + r:
        a += 1
    elif line == x - r or line == x + r:
        b += 1

print(a, b)

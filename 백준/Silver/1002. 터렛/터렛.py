from math import sqrt

t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if dist:
        if dist == (r1 + r2):
            print(1)
        elif dist > (r1 + r2):
            print(0)
        elif dist in (r1 - r2, r2 - r1):
            print(1)
        elif (dist < (r1 - r2)) + (dist < (r2 - r1)):
            print(0)
        else:
            print(2)
    else:
        if (r1 != r2):
            print(0)
        else:
            print(-1)
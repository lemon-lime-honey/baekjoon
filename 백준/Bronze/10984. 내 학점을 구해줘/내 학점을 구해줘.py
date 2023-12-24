t = int(input())

for i in range(t):
    n = int(input())
    total = 0
    gpa = 0.0
    for j in range(n):
        c, g = map(float, input().split())
        total += int(c)
        gpa += g * c
    print(total, gpa / total)
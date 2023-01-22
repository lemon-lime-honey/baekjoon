g, p, t = map(int, input().split())

if (g * p) < (g + t * p):
    print(1)
elif (g * p) > (g + t * p):
    print(2)
else:
    print(0)
a, b, c = map(int, input().split())
calc1 = int(a * b / c)
calc2 = int(a / b * c)
if calc1 < calc2:
    print(calc2)
else:
    print(calc1)
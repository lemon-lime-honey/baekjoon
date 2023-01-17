x, k = map(int, input().split())

if 7 * k <= x:
    print(7 * k * 1000)
elif 3.5 * k <= x:
    print(int(3.5 * k * 1000))
elif 1.75 * k <= x:
    print(int(1.75 * k * 1000))
else:
    print(0)
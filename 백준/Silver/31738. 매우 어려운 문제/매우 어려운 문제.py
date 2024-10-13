n, m = map(int, input().split())

if n >= m:
    print(0)
else:
    calc = 1
    for i in range(n, 0, -1):
        calc = (calc * i) % m
        if calc == 0:
            break
    print(calc % m)

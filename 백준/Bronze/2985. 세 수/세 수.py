a, b, c = map(int, input().split())

if (a + b) == c:
    print(f'{a}+{b}={c}')
elif (a - b) == c:
    print(f'{a}-{b}={c}')
elif (a * b) == c:
    print(f'{a}*{b}={c}')
elif int(a / b) == c:
    print(f'{a}/{b}={c}')
elif a == (b + c):
    print(f'{a}={b}+{c}')
elif a == (b - c):
    print(f'{a}={b}-{c}')
elif a == (b * c):
    print(f'{a}={b}*{c}')
elif a == int(b / c):
    print(f'{a}={b}/{c}')
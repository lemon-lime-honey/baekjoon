a, b, c = map(int, input().split())

if a % 2 and b % 2 and c % 2:
    print(a * b * c)
elif a % 2 and b % 2:
    print(a * b)
elif a % 2 and c % 2:
    print(a * c)
elif b % 2 and c % 2:
    print(b * c)
elif a % 2:
    print(a)
elif b % 2:
    print(b)
elif c % 2:
    print(c)
else:
    print(a * b * c)

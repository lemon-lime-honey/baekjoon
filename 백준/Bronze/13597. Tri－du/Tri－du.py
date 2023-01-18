a, b = map(int, input().split())

if a == b:
    print(a)
else:
    if a < b:
        print(b)
    else:
        print(a)